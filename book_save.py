def log_data(entry):
    with open('book.csv', 'a') as file:
        file.write('{},\n'.format(entry))