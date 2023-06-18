# deleter


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name



    @name.setter
    def name(self, name):
        for sym in name:
            if sym.isdigit():
                raise Exception('Имя недопустимо, так как содержит цифры')

        self.__name = name


    @name.deleter
    def name(self):
        del self.__name

person = Person('Валера', 16)
print(person.name)
person.name = 'Гриша'
print(person.name)
