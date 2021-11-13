'''take two list of same length as input and return a dictionary with one as keys and values other as values.'''

def deccompfor(keys,values):
    d={}
    for i in range(len(keys)):
        d[keys[i]]=values[i]
    print (d)
keys=[1,2,3,4,5]
values=['one','two','three','four','five']
deccompfor(keys,values)