list1=["one",'two','three','four','five']
list2=[1,2,3,4,5,] 
a={}
for i in range(len(list2)):
    a[list1[i]]=list2[i]
print(a)

# a='name', 'sakshi', 'age', '20', 'description', 'ceo of company'
# i=0
# b=[]
# while i<len(a):
#     b.append(a[i])
#     i=i+2
# # print(b)

# c=[]
# i=1
# while i<len(a):
#     c.append(a[i])
#     i=i+2
# # print(c)

# d={}
# for i in range(len(c)):
#     d[b[i]]=c[i]    
# print(d)