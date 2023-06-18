import contextlib


# file = open('test.txt', 'w', encoding='utf-8')
# file.write('веб по контекстному менеджеру')
# file.close()

# with open('test.txt', 'w', encoding='utf-8') as file:
#     file.write('веб по контекстному менеджеру')

# @contextlib.contextmanager
# def reverse_str(string):
#     yield string[::-1]
#
#
# with reverse_str('hello') as reversed_string:
#     print(reversed_string)

@contextlib.contextmanager
def exc_handler(*args):
    try:
        yield
    except args:
        print("Ошибка но мне все равно")


my_list = [1, 2]
my_list.append(3)
my_dict = {1: 1}

with exc_handler(IndexError, AttributeError, KeyError):
    print(my_list.asd)
    my_list[4]
    my_dict[2]

print('Еще какой-то код...')
