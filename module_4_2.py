# Lesson "Пространство имен"

def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()

# inner_function()
'''
При попытке вызова функции inner_function за пределами функции test_function происходит
ошибка: name 'inner_function' is not defined.

'''