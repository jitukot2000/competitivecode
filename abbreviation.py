n = int(input(" "))
list1 = []
for i in range(n):
    str1 = input(" ")
    if len(str1) <= 10:
        list1.append(str1)
    else:
        r = str1[0] + str(len(str1)-2) + str1[-1]
        list1.append(r)
for i in list1:
    print(i)
