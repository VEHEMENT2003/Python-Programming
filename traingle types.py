print("welcome to the triangles")
x=float(input("wirte the x\n"))
y=float(input("wirte the y\n"))
p=float(input("wirte the p\n"))
if((x==y)and(x==p)):
    print("it is an equilateral taingle")

elif((x==y)or(x==p)or(p==x)or(p==y)or(y==x)or(y==p)):
    print("it is an isoceles  taingle")

else:
    print("it is an scalen traingle")
