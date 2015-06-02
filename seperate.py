import csv

with open('input_clean.csv', 'rb') as f:
    reader = csv.reader(f)

    for row in reader:
        with open("./companies/" + row[0].replace("/", "\\") + '.csv', 'a') as w:
            writer = csv.writer(w, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
            writer.writerow(row)
