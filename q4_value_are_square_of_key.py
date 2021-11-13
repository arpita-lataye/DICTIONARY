'''write a python script to print a dictionary that contain a number between 1 and 15(both included)
and value are square of the key.'''

a={}
for i in range(1,16):
    b=i*i
    a.update({i:b})
print(a)