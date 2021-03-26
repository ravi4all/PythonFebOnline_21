# csv - comma separated values
import csv

# with open('poly_data.csv') as file:
#     data = file.read()
#     print(data)

with open('poly_data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
