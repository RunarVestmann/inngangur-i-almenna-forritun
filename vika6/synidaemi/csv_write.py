import csv

FIELDNAMES = ("Date", "Open", "High", "Low", "Close", "Volume", "Adj Close")
with open("google_stock_data.csv", newline="") as file_object:
    writer = csv.DictWriter(file_object, FIELDNAMES)
    writer.writeheader()
    writer.writerow({
        "Date": "8/23/2004",
        "Open": "3",
        "High": "3",
        "Low": "3",
        "Close": "3",
        "Volume": "3",
        "Adj Close": "3"
    })
