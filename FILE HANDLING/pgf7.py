# writing 2 file
fileout=open("f4.txt","w")
for i in range(5):
    name=input("tell name")
    fileout.write(name)
fileout.close()
