# a=[]
# m={}
# for x in range(11,20,1):
#     a.append(x)
#     m.update({'x':a})
# print(m)
# b=[]
# n={}
# for y in range(21,30,1):
#     b.append(y)
#     n.update({'y':b})
# print(n)
# c=[]
# l={}
# for z in range(31,40,1):
#     c.append(z)
#     l.update({'z':c})
# print(l)
# print(a[4])
# print(b[4])
# print(c[4])

dict_nums = dict(x=list(range(11, 20)), y=list(range(21, 30)), z=list(range(31, 40)))
print(dict_nums)
print(dict_nums["x"][4])
print(dict_nums["y"][4])
print(dict_nums["z"][4])
for k,v in dict_nums.items():
       print(k, "has value", v)
