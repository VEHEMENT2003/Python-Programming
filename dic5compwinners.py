n=int(input("how many students ?\n"))
compwinners={}
for a in range(n):
    key=input("name of the student:\n")
    value=int(input("number of competitions won:\n"))
    compwinners[key]=value

    print("the dictionarynoe is :")
    print(compwinners)
