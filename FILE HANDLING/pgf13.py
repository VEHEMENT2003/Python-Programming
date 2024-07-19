# reading and writing operation on same file
count=int(input(" how many students in class"))
fileout=open("marks.txt","a")
for i in range(count):
          print("enter details for student",(i+1),"below:")
          rollno=int(input("tell rn"))
          name=input("tell name")
          marks=float(input(" tell marks"))
          rec=str(rollno)+","+name+","+str(marks)
          fileout.write(rec)
fileout.close()
fin=open("marks.txt")
x=fin.readline()
print(x)
