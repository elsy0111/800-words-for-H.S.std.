import csv

for j in range(1,18):
    for i in range(1,11):
        f = open('D/random' + str(j) + '/Er_' + str(i) + '.csv', 'r', encoding="UTF-8")
        r = open('R/random' + str(j) + '/Er_' + str(i) + '.csv', 'w', encoding="UTF-8")
        reader = csv.reader(f)
        r.write("Eng,Ja" + '\n')
        for i in reader:
            li = str(i[:2])[1:-1]
            li = li.replace("\'","")
            r.write(li + '\n')
        f.close()
        r.close()