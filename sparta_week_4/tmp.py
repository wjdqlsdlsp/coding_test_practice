import csv
 
f = open('../text.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

print(rdr)
f.close()    