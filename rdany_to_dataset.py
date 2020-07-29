import json
L = []

with open("rdany_conversations_2016-03-01.json", "r") as openfile:
    rdany = json.load(openfile)

i = 0
for item in rdany:
    print('rdany:', item)
    print('rdany:', rdany[item])

    for reply in rdany[item]:
        i = i + 1
        print(i, 'reply:', reply["text"])
        L.append({"text":reply["text"], "labels":reply["text"]})


with open("rdany_dataset.txt", "w") as openfile:
    openfile.writelines(L)



# (column1)   (column2)
#   aaa           1
#   bbb           2
import csv

csv_filename = "test.csv"
dict = {'aaa': 1, 'bbb': 2}
with open(csv_filename, 'wb') as f:
    writer = csv.DictWriter(f, delimiter='\t')
    writer.writerows(dict)