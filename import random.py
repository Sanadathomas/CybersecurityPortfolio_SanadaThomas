import random
import string

print('This is the ultimate Password generator!')

length = int(input('Enter the length of password: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols
temp = random.sample(all,length)

Password = "".join(temp)

all = string.ascii_letters + string.digits + string.punctuation


Password = " ".join(random.sample(all,length))

print(Password)
 