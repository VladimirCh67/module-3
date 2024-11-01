
def sum_lst(d_s, s_=0):
    for i in range(len(d_s)):
        a = d_s[i]
        print(a)
        if isinstance(a, int):  # если тип элемента - число, прибавляем его к сумме
            print(s_, ' += ', a)
            s_ += a
            print('s_int ',s_)
        if isinstance(a, str):  # если тип элемента - строка, прибавляем длину строки  к сумме
            print(s_, ' += ', len(a))
            s_ += len(a)
            print('s_str ', s_)
        if isinstance(a, list):  # если тип элемента - спмсок, перебираем его
            print(s_, ' += ', sum_lst(a))
            s_ += sum_lst(a)
            print('s_list ', s_)
        if isinstance(a, dict):  # если тип элемента - спмсок, перебираем его
            print(s_, ' += ', sum_lst(list(a.keys())))
            s_ += sum_lst(list(a.keys()))
            print('s_dck ', s_)
            print(s_, ' += ', sum_lst(list(a.values())))
            s_ += sum_lst(list(a.values()))
            print('s_dcv ', s_)
        if isinstance(a, tuple):  # если тип элемента - спмсок, перебираем его
            print(s_, ' += ', sum_lst(list(a)))
            s_ += sum_lst(list(a))
            print('s_tpl ', s_)

    return s_


def calculate_structure_sum(d_s):
    result_ = 0
    if isinstance(d_s, int):      # если тип элемента - число, прибавляем его к сумме
        result_ += d_s
        print('result_int ', result_)
    if isinstance(d_s, str):      # если тип элемента - строка, прибавляем длину строки  к сумме
        result_ += len(d_s)
        print('result_str ', result_)
    if isinstance(d_s, list):     # если тип элемента - спмсок, перебираем его
        result_ += sum_lst(d_s)
        print('result_list ', result_)
    if isinstance(d_s, dict):     # если тип элемента - спмсок, перебираем его
        result_ += sum_lst(list(d_s.keys()))
        print('result_dck ', result_)
        result_ += sum_lst(list(d_s.values()))
        print('result_dcv ', result_)
    if isinstance(d_s, tuple):     # если тип элемента - спмсок, перебираем его
        result_ += sum_lst(list(d_s))
        print('result_tpl ', result_)

    return result_

data_structure = [

    [1, 2, 3],

    {'a': 4, 'b': 5},

    (6, {'cube': 7, 'drum': 8}),

    "Hello",

    ((), [{(2, 'Urban', ('Urban2', 35))}])

    ]
sum_ = 0

print(data_structure, type(data_structure))
# for i in range(len(data_structure)):
#     a = data_structure[i]
#     print(a, type(a))
#     if isinstance(a, int):      # если тип элемента - число, прибавляем его к сумме
#         sum_ += a
#         print(sum_)
#         continue
#     if isinstance(a, str):      # если тип элемента - строка, прибавляем длину строки  к сумме
#         sum_ += len(a)
#         print(sum_)
#         continue
#     if isinstance(a, list):     # если тип элемента - спмсок, перебираем его
#         for j in range(len(a)):
#             print(a[j], type(a[j]))
#             if isinstance(a[j], int):  # если тип элемента - число, прибавляем его к сумме
#                 sum_ += a[j]
#                 print(sum_)
#             if isinstance(a[j], str):  # если тип элемента - строка, прибавляем длину строки  к сумме
#                 sum_ += len(a[j])
#                 print(sum_)
#     if isinstance(a, dict):  # если тип элемента - словарь, перебираем его
#         print(a.keys())
#         x = list(a.keys())
#         for j in range(len(x)):
#             print(x[j], type(x[j]))
#             if isinstance(x[j], int):  # если тип элемента - число, прибавляем его к сумме
#                 sum_ += x[j]
#                 print(sum_)
#             if isinstance(x[j], str):  # если тип элемента - строка, прибавляем длину строки  к сумме
#                 sum_ += len(x[j])
#                 print(sum_)
#         print(a.values())
#         z = list(a.values())
#         for j in range(len(z)):
#             print(x[j], type(z[j]))
#             if isinstance(z[j], int):  # если тип элемента - число, прибавляем его к сумме
#                 sum_ += z[j]
#                 print(sum_)
#             if isinstance(z[j], str):  # если тип элемента - строка, прибавляем длину строки  к сумме
#                 sum_ += len(z[j])
#                 print(sum_)
#     if isinstance(a, tuple):
#         for j in range(len(a)):
#             print(a[j], type(a[j]))
result = calculate_structure_sum(data_structure)

print(result)

