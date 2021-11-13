k=['a','b','c','d','e']
v=['A','B','C','D','E']
d=dict(zip(k,v))        # zip will create tuple which each element the given list then it convert into a dictionary.
print(d)


for i in zip(k,v):    #if u want to know how zip function work then iteratethr zip and understand
    print(i)                    #('a','A')
                          #('b','B')
                           #('c','C')
                           #('d','D')
                           #('e','E')