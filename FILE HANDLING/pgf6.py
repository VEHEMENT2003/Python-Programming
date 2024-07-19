myfile=open("f2.txt")
str1=" "
size=0
tsize=0
while str1:
    str1=myfile.readline()
    tsize=tsize+len(str1)
    size=size+len(str1.strip())
print("tot size=",tsize)
print("size aftr removal=",size)
