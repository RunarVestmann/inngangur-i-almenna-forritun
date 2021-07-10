import csv

with open("google_stock_data.csv", newline="") as file_object:
    reader = csv.DictReader(file_object)
    for row in reader:
        print(row["Date"])