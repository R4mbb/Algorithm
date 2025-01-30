def bin_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid + 1
        else:
            start = start + 1

    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = bin_search(array, target, 0, n-1)
if result == None:
    print("not found")
else:
    print(result + 1)
