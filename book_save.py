def log_data(first_name):
    with open('book.csv', 'a') as file:
        file.write('antry: {} \n'.format(first_name))