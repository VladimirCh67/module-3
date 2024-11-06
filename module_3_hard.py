def sum_lst(d_s, res_ = 0):

    for i in range(len(d_s)):
        a = d_s[i]

        if isinstance(a, int):  # если тип элемента - число, прибавляем его к сумме
            print(a, ' : число, прибавляем его к сумме')
            res_ += a
        elif isinstance(a, str):  # если тип элемента - строка, прибавляем длину строки  к сумме
            print(a, ' : строка, прибавляем длину строки ', len(a), '  к сумме')
            res_ += len(a)
        elif isinstance(a, list):  # если тип элемента - спмсок, перебираем его
            print(a, ' : список, передаем его в функцию sum_lst, результат прибавляем его к сумме ')
            res_ += sum_lst(a)
        elif isinstance(a, dict):
            print(a, ' : словарь, преобразуем его в список ключей ', list(a.keys()), ' передаем его в функцию sum_lst')
            print(', результат прибавляем к сумме ')
            res_ += sum_lst(list(a.keys()))
            print(' и список значений ',list(a.values()),' передаем его в функцию sum_lst')
            print(', результат прибавляем к сумме ')
            res_ += sum_lst(list(a.values()))
        elif isinstance(a, tuple):
            print(a, ' : кортеж, преобразуем его в список ', list(a), ', ')
            print('передаем его в функцию sum_lst, результат прибавляем его к сумме ')
            res_ += sum_lst(list(a))
        elif isinstance(a, set):
            print(a, ' :  множество, преобразуем его в список ', list(a), ', ')
            print('передаем его в функцию sum_lst, результат прибавляем его к сумме ')
            res_ += sum_lst(list(a))

    return res_

data_structure = [

    [1, 2, 3],

    {'a': 4, 'b': 5},

    (6, {'cube': 7, 'drum': 8}),

    "Hello",

    ((), [{(2, 'Urban', ('Urban2', 35))}])

]


# result = calculate_structure_sum(data_structure)
result = sum_lst(data_structure)

print(result)
