#USing a flipping method
d1={'a':10,'b':20,'c':10}
d2={}

for key,value in d1.items():
    if value not in d2:
        d2[value]=key
    else:
        d2[value].append(key)
print("new dictionary",d2)


# Using a filter method
D1={'a':10,'b':20,'c':10}
D2={}
for i,j in D1.items():
    D2.setdefault(j,set()).add(i)
list1 = list(filter(lambda x: len(x) > 1,D2.values()))
print(list1)
print(len(list1),"values common")

'''
#Removing dupicates
eg_dic={1:111,2:233,3:233,4:344,5:111}
print("The original dictionary is:",eg_dic)
temp={val:key for key,val in eg_dic.items()}
print(temp)
res={val:key for key, val in temp.items()}
print("The dictionary after removing the duplicates is:",res)
'''

