import random as rn
import string
num = int(input("Enter the length of desired password"))
char = string.ascii_letters + string.digits
for i in range (num):
    pw = ''.join(rn.choice(char))
    print(pw , end='')
