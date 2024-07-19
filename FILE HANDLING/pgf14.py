# use of system defined input outpu and error stream
import sys
fh=open("f1.txt")
line1=fh.readline()
line2=fh.readline()
print(line1,line2)
sys.stdout.write(line1)
sys.stdout.write(line2)
