#initialize
e={'name':'john','salary':10000,'age':24}

#Adding key-value pair to empty dictionary
e1={}
e2=dict()
e1['name']='tom'
e1['salary']=12000
e2['name']='vini'
e2['dept']='HR'
print("Creating dict e1",e1)
print("Creating dict e2",e2)

#Using dict() constructor
e3=dict(name='john',salary=12000,dept='Marketing')
print("USing dict() constructor ",e3)
print()
e4=dict({'name':'john','salary':12000,'age':30})
print("Comma-Separated key:value pairs",e4)
print()
#Using zip function
e5=dict(zip(('name','salary','age'),('JOhn',10000,35)))
print("USing zip function",e5)

#in form of sequences
e6=dict([['name','john'],['salary',10000],['age',43]])
print("Created in form of sequences ",e6)

#creating a dictionary from 2 list
keys=['one','two','three']
values=[1,2,3]
numerals=dict(zip(keys,values))
print(numerals)
print()

#nested dictionary
emp={'john':{'age':25,'salary':20000},'Divya':{'age':35,'salary':35000}}
print(emp)


