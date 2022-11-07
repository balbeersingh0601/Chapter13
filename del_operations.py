#Deletion
#using pop() method
Stu={1:'Neha',2:'Salma',3:'Sunaina',4:'Ana',5:"Tarun"}
print(Stu)
print(Stu.pop(3))
print("After using pop method",Stu)
print(Stu.pop(6,'not found'))
print()
#using popitem() method
print(Stu.popitem())
print("After using popitem method",Stu)

#Using clear() method
e={'name':'John','salary':10000,'age':24}
print("After using clear method",e.clear())
print(e)
e1={'name':'Toni','salary':12000,'age':25}
del e1
#print(e1) e1 object not defined




