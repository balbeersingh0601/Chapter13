#Creating dictionaries
'''rno=[]
mks=[]
for a in range(4):
    r,m=eval(input("Enter roll no ,marks "))
    rno.append(r)
    mks.append(m)
d={rno[0]:mks[0],rno[1]:mks[1],rno[2]:mks[2],rno[3]:mks[3]}
print("Created dictionary")
print(d)
if d[2] > 75:
    print("Roll no 2 secured greater than 75")
else:
    print("Roll no 2 secored less than 75")
'''
#Accessing dictionaries
d1={"Vowel1" : 'a',"Vowel2": 'e',"Vowel3":'i',"Vowel4":'o',"Vowel5":'u'}
print(d1.values())
print(d1.keys())

#Input a dictonary
M={}
n=int(input("how many students u want to add "))
for a in range(n):
    r,m=eval(input("Enter roll no, marks "))
    M[r]=m
print("Created dictionary")
print(M)

#Updating a dictonary
print("To modify marks ")
r=int(input("Enter roll no : "))
if r in M:
    M[r]=float(input("Enter new marks"))
else:
    print("No such roll no. found ")
print("Modified dictionary",M)