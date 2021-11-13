'''count the frequency of words appearing in a string'''

user_str=input('enter string:')
a=user_str.split()
d={}
for i in a:
    if i not in d.keys():
        d[i]=0
    d[i]=d[i]+1
print(d)


user_str=input('enter string:')
a=user_str.split()
d={}                           #'here we use python get function which is give in dictionary they work same as above code.'''
for i in a:
    d[i]=d.get(i,0)+1
print(d)