import operator
a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# print('original dictionaly:',a)                    
sorted_a=sorted(a.items(),key=operator.itemgetter(1))
# print('dictionary in ascending order by value:',sorted_a)    '''here we use sorted function to find ascensing order dict item'''

sorted_a=dict(sorted(a.items(),key=operator.itemgetter(1),reverse=True))
# print('dictionary in descending order by value:',sorted_a)    '''here also we use sorted function to find descending order dict item.'''



a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
max=0
b={}
for i in a:
    if a[i]>max:
        max=a[i]
        s=i
# print(max)
a.pop(s)
b.update({s:max})
smax=0
for i in a:
    if a[i]>smax:
        smax=a[i]
        d=i
# print(smax)
a.pop(d)
b.update({d:smax})
tmax=0
for i in a:
    if a[i]>tmax:
        tmax=a[i]
        k=i
# print(tmax)
a.pop(k)
b.update({k:tmax})
fmax=0
for i in a:
    if a[i]>fmax:
        fmax=a[i]
        l=i
# print(fmax)
a.pop(l)
b.update({l:fmax})

hmax=0
for i in a:
    if a[i]>hmax:
        hmax=a[i]
        g=i
b.update({g:hmax})
print(b)             #'''we find descending order dict item with use of for loop'''
                    


# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# max=0
# for i in a:
#     if a[i]>max:
#         max=a[i]
# print(max)