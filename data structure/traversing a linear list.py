def traverse(AR) :
    size = len(AR)
    for i in range (size):
        print(AR[i], end=' ')
#main ,,,,,,,,,,....,

size = int(input("enter the size of linear list:\n"))
AR = [None] * size
print("enter element for the linear list ")
for i in range (size):
    AR[i] = int(input("Element"+str(i) +":\n"))
print("traversing the list:")
traverse(AR)
        
