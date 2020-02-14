""" FOR SOME REASON, THIS ONLY WORKS WITH THE CALIFORNIA HEAD COACHES WIKIPEDIA. """

import sys
import requests
from bs4 import BeautifulSoup
import csv

def get_urls(filename):
	urls = []
	with open(filename, 'r') as f:
		urls.extend(f.readlines())
	return urls

# TODO: Use Wikipedia API instead of BeautifulSoup
def parse_data(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	table = soup.find('table', class_='wikitable').find_all('tr')	
	column_names = [item.text.rstrip() for item in table[0] if item != '\n']

	print(table)
	print(column_names)
	coaches = []
	# first row is the labels, last row is the totals
	for item in table[1:-1]:
		data = item.find_all(['th','td']) # tags in the table
		row = {}
		assert len(data) == len(column_names)
		for i in range(len(data)):
			row[column_names[i]] = data[i].text.rstrip()
		coaches.append(row)
	return coaches

def to_csv(filename, data):
	column_names = data[0].keys()
	with open(filename, 'w', newline='') as output:
		dict_writer = csv.DictWriter(output, fieldnames=column_names)
		dict_writer.writeheader()
		dict_writer.writerows(data)

def main():
	# list of urls
	for i, url in enumerate(get_urls('./data/test_links.txt')):
		data = parse_data(url.rstrip())
		to_csv('./data/test' + str(i) + '.csv', data)
		print("FINISHED URL")

main()
