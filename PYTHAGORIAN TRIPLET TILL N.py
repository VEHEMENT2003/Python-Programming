# PROGRAMME NO - 
#PROGRAMME FOR PYTHAGORIAN TRIPLET TILL n
n=int(input("please tell the number till you want the phythas = "))
for x in range(1,n+1):
    for y in range(1,n+1):
                   for z in range(1,n+1):
                       if((x*x+y*y==z*z)or(z*z+y*y==x*x)or(y*y==z*z+x*x)):
                          print("x:-",x,"y:-",y,"z:-",z)

