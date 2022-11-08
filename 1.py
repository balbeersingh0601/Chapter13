M={}
n=int(input("how many employess u want to add? "))
for a in range(n):
    r,m=eval(input("Enter name, salary "))
    M[r]=m
print("Created dictionary")
print(M)