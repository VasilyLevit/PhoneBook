def get_comand():
    print('1 - добавление записи в книгу')
    return input('Введите номер операции: ')

def get_data():
    book_entry = []
    book_entry.append(input('Введите фамилию: '))
    book_entry.append(input('Введите имя: '))
    book_entry.append(input('Введите номер телефона: '))
    book_entry.append(input('Введите описание: '))
    return book_entry