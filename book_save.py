import csv

def log_data(entry):
    with open('book.csv', 'a', newline='') as file:
        data = csv.writer(file, delimiter = ',')
        data.writerow(entry)