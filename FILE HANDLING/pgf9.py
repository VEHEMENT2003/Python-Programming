# writing 2 file
# overwriting or erasing previous data
fileout=open("f3.txt","w")
for i in range(5):
    name=input("tell name")
    fileout.write(name)
fileout.close()
