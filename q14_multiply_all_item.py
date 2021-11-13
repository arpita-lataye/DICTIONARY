'''write a python program to multiply all the item in a dictionary.'''

d={'x':10,'y':27,'z':34}
result=1
for key in d:
    result=result*d[key]
print(result)