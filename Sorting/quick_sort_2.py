import time
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    print(array)
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

a = time.time()
print(quick_sort(array))
print(time.time() - a)

array = [1, 2, 3, 4, 5, 6, 9, 8, 7]
a = time.time()
print(quick_sort(array))
print(time.time() - a)
