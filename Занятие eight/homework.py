# class Item:
#    def __init__(self, price, brand):
#        self.price = price
#       self.brand = brand
#
#  def __repr__(self):
#       return self.brand
#
#
# items_list = [
#    Item(1000, "Apple"),
#    Item(1200, "Apple"),
#   Item(900, "Samsung"),
#  Item(700, "Samsung"),
#    Item(660, "Xiaomi")
# ]
#
# filter(lambda x: x.brand == 'Xiaomi', items_list)
# print(items_list)

# result = list(filter(lambda x: x.brand == 'Xiaomi', items_list))
# print(result)

names_list = ['данил', 'артём', 'никита', 'влад']
print([x[0].upper() + x[1:] for x in names_list])
