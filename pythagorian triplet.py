#pgm of pythagoriean triplet
num1=int(input("wirte the num1\n"))
num2=int(input("wirte the num2\n"))
num3=int(input("write the num3\n"))
v1=num1*num1
v2=num2*num2
v3=num3*num3
if(v1==v2+v3):
                                  print(num1,num2, "and" ,num3,"from the triplet")
if(v2==v3+v1):
                                  print(num1,num2, "and" ,num3,"from the triplet")  
if(v3==v1+v2):
                                  print(num1,num2, "and" ,num3,"from the triplet")
