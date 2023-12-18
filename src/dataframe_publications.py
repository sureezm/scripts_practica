import csv

#create dataFrame
csvroute= 'src/doi_clean.csv'
pubs=[]

with open(csvroute, newline='') as File:  
    reader = csv.reader(File, delimiter = ';')
    next(File)
    for row in reader:
        id = int(row[0])
        title = row[1]
        doi = row[7]
        pubs.append((id,title,doi))