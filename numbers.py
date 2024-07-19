print("welcome to numbrings")
n1=float(input("wirte the num1\n"))
n2=float(input("write the num2\n"))
print("press + for addition")
print("press - for addition")
print("press * for addition")
print("press / for addition")
opr=input("in put the opression\n")
if(opr=='+'):
    ans=n1+n2
    print("the addition of",n1,"and",n2,"is=",ans)
elif(opr=='-'):
    ans=n1-n2
    print("the substraction of",n1,"and",n2,"is=",ans)
elif(opr=='*'):
    ans=n1*n2
    print("the multiplication of",n1,"and",n2,"is=",ans)
elif(opr=='/'):
    ans=n1/n2
    print("the dividation of",n1,"and",n2,"is=",ans)
else:
    print("your are fool,go kdam mam")
