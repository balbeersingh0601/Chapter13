teams={}
n = int(input("how many teams u want to add "))
for a in range(n):
    t,w,l = eval(input("Enter team_name, matches_won ,matches_lost "))
    teams[t]=[w,l]
print("Created dictionary")
print(teams)