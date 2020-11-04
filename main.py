var_int = 5
var_float = 1.2
var_str = "Hello world"
var_list = ['a', '2']
var_tuple = ('b', '3')
var_dict = {'city': 'Moscow', 'country': 'Russia'}

common_list = [var_int, var_float, var_str, var_list, var_tuple, var_dict]
for i in common_list:
    print(f'{i} is {type(i)}')
