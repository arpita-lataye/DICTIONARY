dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic4={}

for key in dic1:
    if key in dic2:
        dic2[key]=dic1[key]+dic2[key]
    else:
        dic2[key]=dic1[key]
# print(dic2)

for key in dic2:
    if key in dic3:
        dic3[key]=dic2[key]+dic3[key]
    else:
        dic3[key]=dic2[key]
# print(dic3)


for i in (dic1,dic2,dic3):
    dic4.update(i)
print(dic4)