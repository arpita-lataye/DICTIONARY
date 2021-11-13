dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in dict1:
    # print(x)              #thise will print the index.
    # print(dict1[x])       #thise will print the value.
    print(x,'=',dict1[x])   #thise will print both index= value 
    
    
    
    
    
x = dict1.get("model")   #here use get function for print model value.
print(x)



x = dict1.keys()       #o/p= (['brand','model','year'])
print(x)               # here print the list of indexing.
