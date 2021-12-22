x={'key1': 1, 'key2': 3, 'key3': 2}
y={'key1': 1, 'key2': 2}
for i in x:
    for k in y:
        if i=='key1' and k=='key1':
            print(i,'is present in both x and y')
        if i=='key2' and k=='key2':
            print(i,'is present in both x and y')
        else:
            print(i,'is not present in x and y')
