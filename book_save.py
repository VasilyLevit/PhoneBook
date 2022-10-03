import csv

def log_data(entry):
    with open('book.csv', 'a') as file:
        data = csv.writer(file, delimiter = ',')
        data.writerow(entry)