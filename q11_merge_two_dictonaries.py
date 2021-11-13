'''write a python script to merge two python dictionaries.'''

d1={'a':100,'b':200}
d2={'x':300,'y':200}

d=d1.copy()
d.update(d2)
print(d)