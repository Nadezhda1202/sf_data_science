from numpy import *
def cats(a):
    k = 1
    l = 3
                
    for i in range(l-1):
        for j in range(l-1):
            if i == 0 and j == 0 and a[i][j] == 1:
                k += 1
                a[i][j] == k
                if a[i+1][j] == 1:
                    a[i+1][j] == k
                elif a[i][j-1] == 1:
                    a[i][j-1] == k
            elif i == (l-1) and j == 0 and a[i][j] == 1: 
                if a[i][j+1] > 1: 
                    a[i][j] == a[i][j+1]
                elif a[i-1][j] > 1: 
                    a[i][j] == a[i-1][j]
                else:
                    k += 1
                    a[i][j] == k
            elif i == 0 and j == (l-1) and a[i][j] == 1: 
                if a[i][j+1] > 1: 
                    a[i][j] == a[i][j+1]
                elif a[i+1][j] > 1: 
                    a[i][j] == a[i+1][j]
                else:
                    k += 1
                    a[i][j] == k
            elif i == (l-1) and j == (l-1) and a[i][j] == 1: 
                if a[i][j-1] > 1: 
                    a[i][j] == a[i][j-1]
                elif a[i-1][j] > 1: 
                    a[i][j] == a[i-1][j]
                else:
                    k += 1
                    a[i][j] == k
            elif i < (l-1) and j <(l-1): 
                if a[i+1][j] > 1:
                    a[i][j] == a[i+1][j]   
                elif a[i][j+1] > 1: 
                    a[i][j] == a[i][j+1]
                elif a[i-1][j] > 1: 
                    a[i][j] == a[i-1][j]
                elif a[i][j-1] > 1:
                    a[i][j] == a[i][j-1]
                else:
                    k += 1
                    a[i][j] == k
      
    return a

f = open("input.txt")
a = f.read()
result = []
result = cats(a)

print(result)