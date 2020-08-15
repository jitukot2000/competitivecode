s1 = input(" ")  # Take input of string
s2 = input(" ")  # Take second input of string
if s1.lower() == s2.lower():
    print('0')
elif s1.lower() > s2.lower():
    print("1")
else:
    print("-1")
