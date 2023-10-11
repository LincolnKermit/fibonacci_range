import sys

sys.set_int_max_str_digits(100000)

n = int(input('n : '))

temp = 1

t = 1

for i in range(n):       
    temp = temp + t
    t = t + temp

print(t)