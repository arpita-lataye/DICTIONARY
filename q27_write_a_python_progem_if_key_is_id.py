student = [{'id': 1, 'success': True, 'name': 'Lary'},
{'id': 2, 'success': False, 'name': 'Rabi'},
{'id': 3, 'success': True, 'name': 'Alex'}]
sum=0
sum1=0
for i in range(len(student)):
    for d in student[i]:
        if d is 'id':
            sum+=student[i][d]
        if d is 'success':
            sum1+=student[i][d]
print(sum)
print(sum1)