Sample=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1',
'amount': 750}]
b=[]
for i in range(len(Sample)):
    for j,k in Sample[i].items():
        b.append(str(k))
    # print()
        # b.append(k)
# print(b)
# [item, 400, item2, 300, item1,750]
m={}
for i in range(len(b)-2):
    # print(b[i],b[1])
    # print(b[2],b[3])
    # print(b[4],b[5])
    n=(int(b[1])+int(b[5]))
    m.update({b[0]:n})
    m.update({b[2]:b[3]})
    # m.update({b[4]:b[5]})
print(m)
# print(n)