import time
import sys


class CodeTimer:
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time.time()  # засекли наше время (точка старта)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        t = time.time() - self.start  # остановили таймер (точка стопа)
        print(f'Код работал {t} сек.')
        return True


timer = CodeTimer()

with timer as t:
    # # l = [x for x in range(100_000_000)]
    # l = [1, 2, 3]
    # l[5]
    print(t)
    print(1)

# class ThreadRedirect:
#     def __init__(self):
#         self.stdout = sys.stdout
#
#     def __enter__(self):
#         sys.stdout = open('file.txt', 'w', encoding='utf-8')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         sys.stdout = self.stdout
#
#
# with ThreadRedirect():
#     print("Hello, world!")
#
# print("Hello, world!")
