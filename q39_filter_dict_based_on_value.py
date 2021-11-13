di={'cierra vega':175,'alden cantrell':180,'kierra gentry':165,'pierre cox':190}
print('original dictionary',di)

result={key:value for (key,value) in di.items() if value>=170}
print('after filter a dictionary:')
print(result)