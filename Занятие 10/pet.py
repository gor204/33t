# class Pet:
#     has_tail = True
#     legs = 4
#     name = None
#     ears = True
#
#     def __str__(self):
#         return f"У {self.name} {self.legs} ноги и {'есть хвост' if self.has_tail else 'хвоста нет'}." \
#                f"У него {'есть ушки' if self.ears else 'нет ушек'}."
#
#     def sound(self):
#         pass
#
#
# class Dog(Pet):
#     name = 'Чарли'
#
#     def sound(self):
#         return "Гав!"
#
#
# print(Dog())
# print(Dog().sound())
#
#
# class Frog(Pet):
#     has_tail = False
#     ears = False
#     name = "Пе-пе"
#
#     def sound(self):
#         return "Ква!"
#
#
# print(Frog(), Frog().sound())
