#PGM TO CHECK GRETEST AMONG THREE NUMBERS

x=float(input("Tell 1st number")) 
y=float(input("Tell 2nd number"))
z=float(input("Tell 3rd number"))

if(x>y):
    if(x>z):
        print("Among",x,",",y,"and",z,"\nthe gretest no.is=",x)
    else:

        print("Among",x,",",y,"and",z,"\nthe gretest no.is=",z)
elif(y>z):
    print("Among",x,",",y,"and",z,"\nthe gretest no.is=",y)
else:
    print("Among",x,",",y,"and",z,"\nthe gretest no.is=",z)
