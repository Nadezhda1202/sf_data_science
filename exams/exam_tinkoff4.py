n, m = map(int, input().split())
denominations = list(map(int, input().split()))

for d in denominations:
        if d > n:
            denominations.pop(d)
    
dominations = sorted(denominations)

import itertools

numbers = range(3)
combinations = itertools.product(numbers, repeat = m)

has_found = False

for combination in combinations:
    sum = 0
    i = 0
    current = []
    for count in combination:
        sum += count * dominations[i]
        current.append(count)
        i += 1
        if sum == n:
            break
    if sum == n:
        has_found = True
        break
    
if has_found:
    kol = 0
    for i in current:
        kol += i
    print(kol)
    money = ''
    i = 0
    for value in dominations:
        money += (str(value) + ' ') * current[i]
        i += 1
    print(money)
else:
    print(-1)