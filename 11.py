d1={1:11,2:12}
d2={1:11,2:12,3:13,4:15}
#d2={1:11,2:12}
#d1={1:11,2:12,3:13,4:15}
l1=len(d1)
l2=len(d2)
count=0
if(l1<l2):
    for i,j in d1.items():
        for x,y in d2.items():
            if i==x:
                if j==y:
                    count+=1

    if count ==len(d1):
        print("d1 in d2")
else:
    for i, j in d1.items():
        for x, y in d2.items():
            if i == x:
                if j == y:
                    count += 1

    if count == len(d2):
        print("d2 in d1")


