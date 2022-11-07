n=int(input("How many students ?"))
CompWinners={}
for a in range(n):
    key = input("Name of the students")
    value=int(input("No. of competitions won :"))
    CompWinners[key]=value
print("the dictionary now is ")
print(CompWinners)

dic={1:67.3,2:54.5,3:77.9,4:89.5,5:83.5}
print(dic)
rno=int(input("Roll no. to be deleted ?"))
if rno in dic:
    del dic[rno]
    print("Roll no",rno," deleted from dictionary")
else:
    print("Roll no",rno,"does not exist in dictionary")
print("Final Dictionary",dic)