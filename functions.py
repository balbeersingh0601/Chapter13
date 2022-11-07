d={'name':'John','salary':18000,'age':24}
print(len(d))

#Using get() method
print("Using get method, key -> age",d.get('age'))
print("Using get method, key -> name",d.get('name'))

#Using items() method
myList=d.items()
for x in myList:
    print(x)

#Using keys() and values() method
print("Using keys() method ")
print(d.keys())
print("Using keys() method ")
print(d.values())

#Using fromkeys() method
print(d.fromkeys('name','age'),20)
L=[]
n=int(input("How many students ?"))
for a in range(n):
    r=int(input("Enter roll no "))
    L.append(r)
S=dict.fromkeys(L,2500)
print("Created dictionary ",S)
