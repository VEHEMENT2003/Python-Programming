# x raised 2ower y
def x2y(x,y):
    if(y==0):
        return 1
    else:
        return(x*x2y(x,(y-1)))
a=int(input("tell base"))
b=int(input("tell index"))
ans=x2y(a,b)
print(a,"raised 2 power",b," is =",ans)
print("you are very good in calculations dhiraj jadhav")
print("you are fool hahahaha")
