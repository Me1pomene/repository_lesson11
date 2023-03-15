def upper(string):
    '''
    Функция переводит все слово в верхний регистр...
    '''
    return print(string.upper())

def upper_fun(string):
    '''
    Функция переводит первую букву слова в верхний регистр
    '''
    return print(string.title())

string = input('Введите слово')

upper(string)
upper_fun(string)