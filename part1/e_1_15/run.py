import random
import string

number = input('Enter password length: ')
try:
    n = int(number)
except:
    n = len(number)
print(''.join(random.choice(string.ascii_lowercase) for i in range(n)))
