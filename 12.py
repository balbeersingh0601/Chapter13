D1={'A':[1,2,3],'B':[4,5,6],'C':[9,10,11]}
D2={}
D3={}
for i,j in D1.items():
    D2=j
    print(D2)
    print(sum(D2))
    D3[i]=sum(D2)
print(D3)
