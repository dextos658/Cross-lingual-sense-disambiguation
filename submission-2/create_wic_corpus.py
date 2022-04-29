import csv
from os import listdir

files = listdir("corpus")
print(files)

with open("wic_corpus.csv", 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["beseda", "stavek1", "start1", "end1", "stavek2", "start2", "end2"])
    for file in files:
        beseda = file.split('.')[0]

        with open('corpus\\' + beseda + '.csv', 'r', encoding='utf-8') as f1:
            data = list(csv.reader(f1))
            writer.writerow([beseda]+ data[0][1:] + data[1][1:])

