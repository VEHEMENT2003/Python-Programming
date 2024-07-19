# pgm to compute simple intrest
# using positional argument
def si (p1,r1,t1=4):
    intrest=(p1*r1*t1)/100
    print("principal intrest =",p1,"rate of intrest=",r1,"time period =",t1)
    print("simple itresrt =",intrest)




p1=float(input("tell principal amount"))
r1=float(input("tell rate of intrest"))
t1=float(input("tell time period"))
si(p1,r1)
