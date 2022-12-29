import csv
import random 

f = open('E800.txt', 'r', encoding="UTF-8")
arr = []
reader = csv.reader(f)

for line in reader:
    arr.append(line)

f.close()

for j in range(1,18):
    n = open('D/random_all/Er_a' + str(j) + '.txt', 'w', encoding="UTF-8")
    a = arr
    random.shuffle(a)
    n.write(str(a))
    n.close()

    k = open('D/random_all/Er_a' + str(j) + '.csv', 'w', encoding="UTF-8")
    for i in a:
        s = str(i)[1:-1]
        s = s.replace("\'","")
        s = s.replace(" ","")
        # s = s.replace("\'","\"")
        k.write(s + "\n")
    k.close()

    n = open('D/random17/Er_' + str(j) + '.txt', 'w', encoding="UTF-8")
    a = arr[800:842]
    random.shuffle(a)
    n.write(str(a))
    n.close()


    k = open('D/random17/Er_' + str(j) + '.csv', 'w', encoding="UTF-8")
    for i in a:
        s = str(i)[1:-1]
        s = s.replace("\'","")
        s = s.replace(" ","")
        # s = s.replace("\'","\"")
        k.write(s + "\n")
    k.close()

    for i in range(16):
        n = open('D/random' + str(i + 1) + '/Er_' + str(j) + '.txt', 'w', encoding="UTF-8")
        a = arr[i * 50 : (i + 1) * 50]
        random.shuffle(a)
        n.write(str(a))
        n.close()

        k = open('D/random' + str(i + 1) + '/Er_' + str(j) + '.csv', 'w', encoding="UTF-8")
        for i in a:
            s = str(i)[1:-1]
            s = s.replace("\'","")
            s = s.replace(" ","")
            # s = s.replace("\'","\"")
            k.write(s + "\n")
        k.close()