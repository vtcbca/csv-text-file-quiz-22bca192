import csv
with open('C://22BCA192//PYTHON//contact1.csv','w',newline='') as obj:
    p=csv.writer(obj)
    h=['name','contact']
    p.writerow(h)
    data=[['om',1234567890],
          ['sai',1223456789],
          ['ram',1234455777],
         ['radha',1234455777],
         ['gopal',345678902]]
    p.writerows(data)
with open('C://22BCA192//PYTHON//contact1.csv','r',newline='') as ob:
    r=csv.reader(ob)
    for j in r:
         print(j)
         
with open('C://22BCA192//PYTHON//contact1.csv','r',newline='') as o:
    head=next(o)
    r=csv.reader(o)
    name=input("Enter the name of student:")
    for i in r:
        if i[0]==name:
             print(i)





             
