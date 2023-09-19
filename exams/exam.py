
n_t = input()
a = input() #время на каждого пациента

n_t = n_t.split(' ')

n = int(n_t[0]) #количество пациентов
t = int(n_t[1]) #максимальное количество времени

a = a.split(' ')
b = []
for i in a:
    b.append(int(i))
    if len(b) >= n:
        break
b = sorted(b)
sum = 0
result = 0
for i in b:
    sum += i
    if sum <= t:
        result += 1
    else:
        break
            
print(result)