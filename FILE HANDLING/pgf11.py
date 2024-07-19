# writing 2 file if file not existing....it is created automatically
# appending over previous data
fileout=open("f7.txt","a")
for i in range(5):
    name=input("tell name")
    fileout.write(name)
fileout.close()
