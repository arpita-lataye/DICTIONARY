'''write a python program to create and display all combinations of letters, selecting each letter from a differentrew key in a dictionary.'''
a={'1':['a','b'],'2':['c','d']}
for key in (a):
    for j in (a[key]):
        print(key*a[1][j])
