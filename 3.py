d={1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',0:'Zero'}
n=int(input("Enter the no."))
r=0
while n!=0:
    a=n%10
    n=n//10
    r=r*10+a
print("Revered no",r)
while r!=0:
    d1=r%10
    r=r//10
    for i in d:
        if d1==i:
            print(d[i],end=" ")
