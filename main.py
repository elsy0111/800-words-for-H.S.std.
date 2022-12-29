import csv

n = open('E800_New.txt', 'w', encoding="UTF-8")
# f = open('E800', 'r', encoding="shift_jis")
f = open('E800.txt', 'r', encoding="UTF-8")

reader = csv.reader(f)
for line in reader:
    l = []
    print(line)
    for i in line[1:]:
        if len(i) != 0:
            l.append(i)
    l = str(l)[1:-1]
    l = l.replace("\'","")
    l = l.replace(" ","")
    n.write(line[0] + "," + l + "\n")
f.close()