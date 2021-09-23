import csv
import json
import sys

input = sys.argv[1]
outpout = sys.argv[2]

inputFile = open(input) 
outputFile = open(outpout, 'w') 

data = json.load(inputFile) 

inputFile.close()

output = csv.writer(outputFile)

output.writerow(data[0].keys()) 

for row in data:
    output.writerow(row.values()) 