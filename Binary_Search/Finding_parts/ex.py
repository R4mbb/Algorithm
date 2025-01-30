import sys
input = sys.stdin.readline

# =======  이진탐색  =================================================================================

def bin_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        print(array[mid], target)

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

n = int(input().rstrip())
array = list(map(int, input().split()))
array.sort()


m = int(input().rstrip())
x = list(map(int, input().split()))

for i in x:
    result = bin_search(array, i, 0, n-1)

    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
print(array)



# =======  계수정렬  =================================================================================

n = int(input().rstrip())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1


m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

#print(array)



# =======  집합 자료형  =================================================================================

n = int(input().rstrip())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')

print(array)
