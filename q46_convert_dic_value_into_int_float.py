'''Q46.Write a Python program to convert string values of a given dictionary, into integer/float
datatypes. Go to the editor'''


a=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
for dict in a:
    for i in dict:
        dict[i]=int(dict[i])
print(str(a))

b=[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
for dicts in b:
    for i in dicts:
        dicts[i]=float(dicts[i])
print(b)