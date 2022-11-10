teams={}
d2={}
d3={}

n = int(input("how many teams u want to add "))
for a in range(n):
    t,w,l = eval(input("Enter team_name, matches_won ,matches_lost "))
    teams[t]=[w,l]
print("Created dictionary")
print(teams)
for i,j in teams.items():
    d2=j
    d3[i]= sum(d2)
team_inquiry= input("Enter the team to know its winning percentage")
for i in d3:
    if i==team_inquiry:
        print("No. of matches played by ",i,"are",d3[i])

