# writing 2 file
# appending over previous data
fileout=open("f3.txt","a")
for i in range(5):
    name=input("tell name")
    fileout.write(name)
fileout.close()
