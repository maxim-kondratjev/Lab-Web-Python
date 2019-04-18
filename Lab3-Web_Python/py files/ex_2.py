#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['a', 'b', 'C', 'c']
print(list(data2))
print("-----------------")
# Реализация задания 2
i = Unique(data3, ignore_case=True)
for _ in range(i.size):
    print(next(i), end=" ")
print("\n-----------------")

a = Unique(gen_random(1, 3, 10))
for _ in range(a.size):
    print(next(a), end=" ")