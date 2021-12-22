dict = {'a': {'1','2'}, 'b':{'5','1'}, 'c':{'3','2'}}
output = {}

for key, value in dict.items():
    for v in value:
        if v in output.keys():
            output[v].append(key)
        else:
            output[v] = [ key ]

print(output)