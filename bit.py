flag = 0
sum1 = 0
n = int(input(" "))
for i in range(0,n):
    x = input(" ")
    if x == "X++" or x == "++X":
        flag = 1
    elif x == "--X" or x == "X--":
        flag = -1
    sum1 = sum1 + flag
print(sum1)