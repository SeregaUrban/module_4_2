def test_function():
    # inner_function()
    def inner_function():
        return print('Я в области видимости функции')
    return  inner_function()
test_function()
# inner_function()