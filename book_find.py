def find_data(find_str):
    # path = 'book.csv'
    data = open('book.csv', "r")
    for line in data:
        result = []
        if find_str in line:
            result.append(line)
        else:
            result.append('Не найдено')
    data.close()
    return result