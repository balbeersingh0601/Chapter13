M={'jan':31,'feb':28,'march':31,'april':30,'may':31,'june':30,'july':31,'aug':31,'sep':30,'oct':31,'nov':30,'dec':31}
print("The hardcoded dictionary",M)
month=input("Enter the month to find the no. of days in it")
for a in M:
    if a == month:
        print("The no. of days in",a,"are",M[a])

dic_sort=sorted(M)
print("Months in sorted order ",dic_sort)
print()
dic_sort_key_value=sorted(M.items())
print("Whole dictionary is sorted",dic_sort_key_value)
print()
print("The month with 31 days are")
for a in M:
    if M[a]==31:
        print(a,end=' ')


