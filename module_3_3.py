def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

value_list = [25, False, 'новая строка']
value_dict = {'a' : True, 'b' : 165, 'c' : 'String'}

print_params(*value_list)
print_params(**value_dict)

values_list_2 = [True, '5 строка']

print_params(*values_list_2, 42)


