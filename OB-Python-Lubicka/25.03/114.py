
import csv
start = int(input ("Enter a starting year: ")) 
end=int(input ("Enter an end year: "))
file = list(csv.reader (open ("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)
X = 0
for row in tmp:
    if int (tmp[x][2]) >= start and int(tmp[x] [2]) <=end:
        print (tmp [x])
    x = x+1