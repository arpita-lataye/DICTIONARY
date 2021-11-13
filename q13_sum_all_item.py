''' write a python program to sum all the item of a dictionary.'''

sum=0
d={'x':10,'y':20,'z':30}
for i in d:
    sum=sum+d[i]
print(sum)