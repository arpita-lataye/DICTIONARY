my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    }
a=[]
max=0
for i in my_dict:
    if my_dict[i]>max:
        max=my_dict[i]
        s=i
a.append(s)
# print(s)
my_dict.pop(s)
smax=0
for i in my_dict:
    if my_dict[i]>smax:
        smax=my_dict[i]
        h=i
a.append(h)
# print(h)
my_dict.pop(h)
tmax=0
for i in my_dict:
    if my_dict[i]>tmax:
        tmax=my_dict[i]
        k=i
a.append(k)
# print(k)   
print(a)     