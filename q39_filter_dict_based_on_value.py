di={'cierra vega':175,'alden cantrell':180,'kierra gentry':165,'pierre cox':190}
print('original dictionary',di)

# result={key:value for (key,value) in di.items() if value>=170}
# print('after filter a dictionary:')
# print(result)

Original={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
a={}
for i,j in Original.items():
    # print(j)
    if j>170:
        # print(j)
        a.update({i:j})
print(a)