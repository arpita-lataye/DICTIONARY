'''write a python program to remove a key from a dictonary.'''

my_dict={'a':1,'b':2,'c':3,'d':4}
print(my_dict)
if 'a' in my_dict:
    del my_dict['a']
print('dictionary after deleting',my_dict)