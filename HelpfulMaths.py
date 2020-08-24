"""
Input
The first line contains a non-empty string s — the sum Xenia needs to count. String s contains no spaces. It only contains digits and characters "+". Besides, string s is a correct sum of numbers 1, 2 and 3. String s is at most 100 characters long.

Output
Print the new sum that Xenia can count
Input = 3+2+1
Output = 1+2+3"""

s = input(" ")
list1 = s.split('+')
list1.sort()
s1 = "+".join(list1)
print(s1)

    