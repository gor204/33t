from time import time

r, t = range(1, 1000001), time()
A = [i * i for i in r];
T = time();
print(T - t)
A = [i ** 2 for i in r];
t = time();
print(t - T)
B = (i * i for i in r);
T = time();
print(T - t)
B = (i ** 2 for i in r);
print(time() - T);
input()
