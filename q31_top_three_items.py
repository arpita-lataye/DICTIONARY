my_dict={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55,'item5': 24}
max=0
n={}
m={}
k={}
a={}
for i in my_dict:
    # print(my_dict[i])
    if my_dict[i]>max:
        max=my_dict[i]
        s=i
# print(max)
n.update({i:max})
# print(n)
my_dict.pop(s)
smax=0
for i in my_dict:
    if my_dict[i]>smax:
        # if smax!=max:
            smax=my_dict[i]
            h=i
# print(smax)
m.update({i:smax})
# print(m)
my_dict.pop(h)
tmax=0
for i in my_dict:
    if my_dict[i]>tmax:
        # if tmax!=max and tmax!=smax:
            tmax=my_dict[i]
# print(tmax)
k.update({i:tmax})
# print(k)

for w in (n,m,k):
    a.update(w)
    print(a)