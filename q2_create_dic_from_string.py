# write a python program to create a dictionary from string.

str1='w3resource'
a={}
for letter in str1:
    a[letter]=a.get(letter,0)+1
print(a)