import json
sentence="This is a super idea "
words=sentence.split()
d={}
for one in words:
    key=one
    if key not in d:
        count=words.count(key)
        d[key]=count
print("Counting frequencies in list",words)
print(json.dumps(d,indent=1))