print("Set default for the dictionary")
d={}
v1=d.setdefault(30,'r')
v2=d.setdefault(30,'rr')
v3=d.setdefault(40)
print(v1,v2,v3)

Marks={1:350,2:423,3:411,4:300}
Marks.setdefault(5,320)
print("Keys is not already present",Marks)
Marks.setdefault(5,340)
print("After updating again, key is already present ", Marks)