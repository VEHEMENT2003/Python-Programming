print("enter six no.s below")
num1=float(input("first number:\n"))
num2=float(input("second number:\n"))
num3=float(input("third number:\n"))
num4=float(input("fourth number:\n"))
num5=float(input("fivfth number:\n"))
num6=float(input("sixth number:\n"))
divisor = float(input("enter divisor number:\n"))
count = 0
print("multiples of ",divisor,"are:")
remainder = num1 % divisor
if remainder == 0:
    print(num1,sep =" ")
    count + 1
remainder = num2 % divisor
if remainder == 0:
    print(num2,sep =" ")
    count + 1
remainder = num3 % divisor
if remainder == 0:
    print(num3,sep =" ")
    count + 1
remainder = num4 % divisor
if remainder == 0:
    print(num4,sep =" ")
    count + 1
remainder = num5 % divisor
if remainder == 0:
    print(num5,sep =" ")
    count + 1
remainder = num6 % divisor
if remainder == 0:
    print(num6,sep =" ")
    count + 1
print()
print(count,"multiples of ",divisor,"found")
