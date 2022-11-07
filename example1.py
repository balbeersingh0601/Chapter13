#7
d1={'Bhavna':1,'Richard':2,"Firoza":3,'Arsh':4}
temp=""
for key in d1:
    if temp<key:
        temp=key
print(temp)

d1={'Bhavna':1,'Richard':2,"Firoza":3,'Arsh':4}
k="Bhavna"
v=-1
if k in d1:
    d1[k]=v
print(d1)

#8
D={'a':2,'b':3,'c':1}
E={}
for c in D:
    E[D[c]]=c
print(E)

#10
num={33:455,23:670,13:500,3:311}
size=len(num)
for i in range(size):
    x=num.popitem() #ek ek item dictionary nikl rha h
    if len(num)>0:
        print("Key-value-pair",x)
        print("Now dict size is ",len(num))

#12
