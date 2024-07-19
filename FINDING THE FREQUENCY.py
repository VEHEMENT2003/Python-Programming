# PROGRAMME NO - 
# FOR FINDING THE FREQUENCY IN A SENTENCE
import json
sentence = ("This is a super idea this \
idea will change the idea of learning")
words=sentence.split()
d={}
for one in words:
    key=one
    if key not in d:
        count=words.count(key)
        d[key]=count
print("Counting frequencies in list \n",words)
print(json.dumps(d,indent=1))
