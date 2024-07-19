# to get totale of marks  using alphabets
 # function exucation
def marks (x,y,z,v,h):
    s=x+y+z+v+h
    d=s/500*100
    return s,d

#main
sub1=float(input("enter maths marks:\n"))
print("out of 100")
sub2=float(input("enter physics marks:\n"))
print("out of 100")
sub3=float(input("enter chemistry marks:\n"))
print("out of 100")
sub4=float(input("enter computer marks:\n"))
print("out of 100")
sub5=float(input("enter english marks:\n"))
print("out of 100")
marks =marks(sub1,sub2,sub3,sub4,sub5)
print("totale marks of student and percentage of student  \n ",marks)
print("marks out of 500 and percentage of student")
