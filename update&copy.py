#Updating
e1={'name':'John','salary':10000,'age':24}
e2={'name':'Diya','salary':12000,'age':28,'dept':'Sales'}
e1.update(e2)
print("Updated dictionary",e1)

#Copying using copy() method
e3=e1.copy()
print("After copying the dictionary, e3",e3)
e1['dept']='HR'
print("Original dict after updating department", e1)
print("Copyied dict, no changes",e3)
print()

#if keys are mutable(lists)
d1={1:[1,2,3],2:[3,4,5]}
d2=d1.copy()
d2[1].append(4)
print(d1)
print()

#Copying using assignment operator
e4=e1
print("After copying the dictionary, e4",e4)
e1['salary']=20000
print("Original dict, after modifying salary", e1)
print("Copyied dict, changes r reflected ",e4)
print()


#Another example
old={'name':'Vini','age':25}
new=old.copy()
new['name']='Tom'
print("Old dictionary",old)
print("Updated dictionary",new)
print()

old1={'name':['Vini','Rini'],'age':[25,23]}
new1=old1.copy()
new1['name'].append('Tony')
print("Old dictionary",old1)
print("Updated dictionary",new1)


