# number = 10
# number2 = 20
#
#
# # Сложение
# print(number + number2)
#
# # Вычитание
# print(number - number2)
#
# # Обычное деление
# print(number / number2)
#
# # Деление нацело
# print(number // number2)
#
# # Деление по остатку
# print(number % number2)
#
# # Умножение
# print(number * number2)
#
# # Возведение в степень
# print(number ** number2)
# try:
#     name = input("Введите ваше имя: ")
#     age = int(input("Сколько вам лет? "))
# except (ValueError, InterruptedError, IndexError):
#     print("Блок except. В переменную age было подано не число. Исправьте ошибку.")
# except AttributeError:
#     print("...")
# else:
#     print(f"Блок else. Тебя зовут {name}! Тебе {age} лет!")
# finally:
#     print("Блок finally. Программа завершена.")

# 1 способ (НЕ ИСПОЛЬЗУЕМ)
# print("Тебя зовут " + name + "! " + "Тебе " + str(age) + " лет!")

# 2 способ (ИСПОЛЬЗУЕМ)
# print("Тебя зовут {username}! Тебе {user_age} лет!".format(
#                    username=name,   user_age=age
# ))
#
# print("Тебя зовут {}! Тебе {} лет!".format(name, age))

# 3 способ (ИСПОЛЬЗУЕМ)

# Тебя зовут [name]! Тебе [age] лет!
# 0.5, 0.5 = 10 * 0.05, 100 * 0.005, 1000 * 0.0005, 5 * 10 ^(-1)

# numbers_list = [1, 2, 3, 4, 5]
# numbers_list.append(1_000_000_000)
# numbers_list.append(0)
# numbers_list.append(10)
# print(numbers_list[0])
# print(numbers_list[-1])
# print(numbers_list[1:4])
# print(numbers_list[::-1])

# def summa(a, b):
#     return a + b
#
#
# result = summa(100, 50)
# print(result ** 2)


