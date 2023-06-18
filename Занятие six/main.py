# class Year:
#     def __init__(self):
#         self.__days = 365
#         self.__season = 'лето'
#
#     def get_days(self):
#         return self.__days
#
#     def set_days(self, days):
#         if days == 365 or days == 366:
#             self.__days = days
#         else:
#             raise Exception(f'Вы передали некорректное значение, в году не может быть {days} дней.')
#
#
# year = Year()
# print(year.get_days())
# year.set_days(364)
# print(year.get_days())

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         for sym in name:
#             if sym.isdigit():
#                 raise Exception('Имя недопустимо, так как содержит цифры')
#
#         self.__name = name
#
#
# person = Person('Валера123', 16)
# print(person.name)
# person.name = 'Гриша'
# print(person.name)





class Spisok(list):
    def delete_last_item(self):
        self.remove(self[-1])

my_l = Spisok()
my_l.append(1)
my_l.append(2)

my_l.delete_last_item()
print(my_l)





