#printing lines in rev manner
fin=open("data.txt")
linelist=fin.readlines()
w=len(linelist)
#print(linelist)
for x in  range(-1,-w,-1):
    print(linelist[x])
