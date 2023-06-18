class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __radd__(self, other):
        if isinstance(other, int):
            return self.price + other
        elif isinstance(other, Item):
            return self.price + other.price

    def __add__(self, other):
        if isinstance(other, int):
            return self.price + other
        elif isinstance(other, Item):
            return self.price + other.price

    def __sub__(self, other): #вычитание
        if isinstance(other, int):
            return self.price - other
        elif isinstance(other, Item):
            return self.price - other.price

    def __mul__(self, other): #умножение
        if isinstance(other, int):
            return self.price * other
        elif isinstance(other, Item):
            return self.price * other.price

    def __truediv__(self, other): #деление
        if isinstance(other, int):
            return self.price / other
        elif isinstance(other, Item):
            return self.price / other.price

item1 = Item('Видеокарта', 15_000, 0.8)
item2 = Item('Процессор', 20_000, 0.2)
item3 = Item('Оперативка', 8_000, 0.2)
item4 = Item('Блок итания', 8_000, 0.3)
total_sum = item1 + item2 + item3
total_sub = item1 - item3
total_mul = item1 * item3
total_truediv = item1 / item4

# total_sum = 1000 + item1 != item1 + 1000
print(total_sum)
print(total_sub)
print(total_mul)
print(total_truediv)
