n = int(input())  
result = 0
for i in range(1,n+1): 
    p,v,t = map(int, input(" ").split())
    if p == 1 and v == 1 and t == 1:
        result = result + 1
    elif p == 1 and v == 1:
        result = result + 1
    elif v == 1 and t == 1:
        result = result + 1
    elif p == 1 and t == 1:
        result = result + 1
print(result)


