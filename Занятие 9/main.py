# def func(a, b, *args, **kwargs):
#     print(a, b)
#     print(args)
#     print(kwargs.get('name_3'))
#
#
# func(10, 20, 30, 40, 50, 60, 70, 'Алина', 'Дамир', 'Булат', name='Ксюша', name_2='Ахмед', name_3='Рома')

# def func(a, b="Apple"):
#     print(a, b)


# func(10, "Samsung")
# func(a="Apple", 10)

# age = 18

# if age >= 18:
#     is_allow = 'Можно'
# else:
#     is_allow = 'Нельзя'

# print(is_allow)
# citizenship = "Казахстан"
# is_allow = 'Можно' if age >= 18 and citizenship == "РФ" else 'Нельзя'
# print(is_allow)

# a = 1000
# b = 100
#
# c = b or a
#
# print(c)

# my_list = []
#
# for i in range(1000):
#     my_list.append(i)

# my_list = [i if i % 3 == 0 else i ** 2 for i in range(1000) if i % 5 == 0]
#
# print(my_list)

# my_dict = {i: len(i) for i in ['orange', 'green', 'blue'] if len(i) != 5}
# print(my_dict)

# my_list_1 = [1, 2]
# my_list_2 = [1, 2]

# my_list_1.append(3)

# a = 20
# b = 20

# print(my_list_1 == my_list_2)
# print(my_list_1 is my_list_2)
# print(a is b)
# print(id(a), id(b))
# print(id(my_list_1), id(my_list_2))

# my_tuple = (1, 2, 3, 4, 5)
# print(type(my_tuple))
# print(my_tuple.index(4))
# print(my_tuple.count(4))
# print(my_tuple[2:4])

# my_tuple = tuple(i for i in range(1000))
# print(my_tuple)

# my_list = [1, 1, 2, 3, 4, 4]
# my_set = set(my_list)
# print(my_set)

# my_set = {1, 2, 3, 4, 5}
# my_set_2 = {4, 5, 6, 7, 8}
# print(my_set.intersection(my_set_2))
# print(my_set.union(my_set_2))
