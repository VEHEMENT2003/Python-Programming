Employee={'john':{'age':25,'salary':20000},'diya':{'age':35,'salary':50000}}
for key in Employee:
    print("employee",key,':')
    print('age:',str(Employee[key]['age']))
    print('salary:',str(Employee[key]['salary']))
