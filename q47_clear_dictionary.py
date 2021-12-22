# Q47.
'''A Python Dictionary contains List as value. Write a Python program to clear the list values in
the said dictionary.'''

a={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
for key in a:
    a[key].clear()
print(a)