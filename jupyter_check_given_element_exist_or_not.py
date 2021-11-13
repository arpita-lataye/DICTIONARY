'''check if a given key exists in a dictionary or not'''
d={'suresh':556,'ramesh':557,'ganesh':558,'umesh':590}
user_ip=input('enter the key to be verified :')
if user_ip in d.keys():
    print('key is present in the dictionary')
    print('value',':',d[user_ip])
else:
    print('key does not present in the dictionary')