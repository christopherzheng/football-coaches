import csv

with open('./data/coaches/california.csv') as f:
	dict_reader = csv.DictReader(f)
	data = []
	for row in dict_reader:
		data.append({key: value for (key, value) in row.items() if key != 'No.'})
		
with open('./data/coaches/california.csv', 'w') as f:
	dict_writer = csv.DictWriter(f, fieldnames=data[0].keys())
	dict_writer.writeheader()
	dict_writer.writerows(data)