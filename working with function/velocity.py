# to get velocity of vehicle  using alphabets
 # function exucation
def velocity (x,y):
    s=x/y
    return s

#main
num1=float(input("enter speed of the vehicle:\n"))
print("km/h")
num2=float(input("enter distance of vehicle:\n"))
print("km")
velocity =velocity(num1,num2)
print("velocity of a vehicle is \n ",velocity)
