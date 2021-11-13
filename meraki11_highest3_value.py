my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }

max=0
for i in my_dict:
    # print(my_dict[i])
    if my_dict[i]>max:
        max=my_dict[i]
        s=i
print(max)
my_dict.pop(s)
smax=0
for i in my_dict:
    if my_dict[i]>smax:
        # if smax!=max:
            smax=my_dict[i]
            h=i
print(smax)
my_dict.pop(h)
tmax=0
for i in my_dict:
    if my_dict[i]>tmax:
        # if tmax!=max and tmax!=smax:
            tmax=my_dict[i]
print(tmax)