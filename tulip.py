n=int(input("how many lines you want"))
t=int(input("which sign you want"))
for x in range(n,1,-1):
    print(t)
    for y in range(1,x+1):
        print("t",end=" ")
