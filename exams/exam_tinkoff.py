def find_expensive_revolver(s, prices):
    affordable_prices = [price for price in prices if price <= s]
    if len(affordable_prices) == 0:
        return 0
    else:
        max_price = max(affordable_prices)
        return max_price

s_n = input() 
s_n = s_n.split(' ')

n = int(s_n[0]) # оставшиеся деньги у ковбоя
s = int(s_n[1]) # количество револьверов в магазине

a = input() # цены на доступные револьверы

a = a.split(' ')
prices = []
for i in a:
    prices.append(int(i))
    if len(prices) >= n:
        break


expensive_revolver = find_expensive_revolver(s, prices)
print(expensive_revolver)