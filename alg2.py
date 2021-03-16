import random
import timeit

random.seed(3)
my_array = [random.randint(0,99) for _ in range(10000)]
# print(my_array)
my_array_sorted = sorted(my_array)
# print(my_array_sorted)

# 選択ソート関数を実装する
def selection_sort(array):
    x = array.copy()
    n = len(x)
    for i in range(n):
        min_idx = i
        for j in range(i,n):
            if x[j] < x[min_idx]:
                min_idx = j
        x[i], x[min_idx] = x[min_idx], x[i]

    return x

print(timeit.timeit('selection_sort(my_array)', globals = globals(), number=1))
print(timeit.timeit('sorted(my_array)', globals = globals(), number=1))