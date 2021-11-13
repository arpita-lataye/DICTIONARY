'''write a python program to get the maximum and minimum value in a dictionary.'''

d={'x':500,'y':5874,'z':560}
key_max=max(d.keys(),key=(lambda k:d[k]))
key_min=min(d.keys(),key=(lambda k:d[k]))

print('maximum value:',d[key_max])
print('minimum value:',d[key_min])