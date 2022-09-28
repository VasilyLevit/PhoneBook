def get_data(first_name):
    with open('book.csv', 'a') as file:
        file.write('FirstName: {} \n'.format(first_name))