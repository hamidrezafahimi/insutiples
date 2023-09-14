import csv   
fields=[1,2,3,4,5,6,7,8,9]
with open('file.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(fields)