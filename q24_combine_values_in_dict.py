'''write a python program to combine values in python list of dictionaries.'''

data=[{'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]
 


from pprint import pprint
dict_nums=(dict(x=list(range(11,20)),y=list(range(21,30)),z=list(range(31,40))))
pprint(dict_nums)
print(dict_nums['x'][4])
print(dict_nums['y'][4])
print(dict_nums['z'][4])
for k,v in dict_nums.items():
    print(k,'has value',v)