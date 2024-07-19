# writing 2 file
fileout=open("f5.txt","w")
for i in range(5):
    name=input("tell name")
    fileout.write(name)
    fileout.write("\n")
fileout.close()
