import csv

with open('new_animal.csv', 'r') as f: 
	animals = csv.reader(f)
	for row in animals: 
		print("reading row")
		if row[-1] ==  "TRUE": 
			print("{0} is a {1} and is house broken".format(row[0], row[1]))
		elif row[-1] == "FALSE": 
			print("{0} is a {1} and is not house broken".format(row[0], row[1]))