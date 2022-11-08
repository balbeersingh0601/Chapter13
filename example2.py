#values of common keys r added in third dictionary

dct1={'1':100,'2':200,'3':300}
dct2={'1':300,'2':200,'4':400}
dct3=dict(dct1)
dct3.update(dct2)

for i,j in dct1.items():
    for x,y in dct2.items():
        if i==x:
            dct3[i]=(j+y)
print("Two given dictionaries are :")
print(dct1)
print(dct2)
print("The resultant dictionary")
print(dct3)