#PGM TO FIND THE H.C.F. OF TWO INPUTE NUMBER
#DEFINE A FUNCTION
num1=int(input("Enter the number"))
num2=int(input("Enter the number"))
def computerHCF(x,y):
    #CHOSE THE SMALLER
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if ((x%i==0)and(y%i==0)):
            HCF=i
            return HCF
    #num1=int(input("Enter the number"))
    #num2=int(input("Enter the number"))
    print("the hcf of",num1,"and",num2,"is", computerHCF(num1,num2))
