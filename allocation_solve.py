t = int(input())

test_case = 1

while t > 0:
    n, b = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()

    count = 0

    for i in a:
        if i <= b:
            b -= i
            count += 1

    print(f'Case #{test_case}: {count}')
    test_case += 1

    t -= 1