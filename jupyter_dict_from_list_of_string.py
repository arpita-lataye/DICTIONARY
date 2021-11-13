user_str=input('enter string:')
words=user_str.split()
d={}
for str in words:
    ch=str[0]
    if ch not in d:
        d[ch]=[]
    d[ch].append(str)
print(d)

for k,v in d.items():
    print(k,':',v)