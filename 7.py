M={}
#n=int(input("how many students u want to add "))
for a in range(2):
    r,n,m,g=eval(input("Enter roll no, name,marks, grade  "))
    M[r]=n,m,g
print("Created dictionary for 2 students, change the loop count for 10 students")
print(M)