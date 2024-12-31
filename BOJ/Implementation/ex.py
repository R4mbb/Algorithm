n = int(input())


for _ in range(n):
    data = input()
    result = 0
    oc = 0

    for i in data:
        if i == 'X':
            oc = 0
            continue

        oc += 1
        result += oc

    print(result)
