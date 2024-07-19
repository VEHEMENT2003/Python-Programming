# PROGRAMME NO - 
#BUBBLE SORTING
aList=[15,6,13,22,3,52,2,546,46,879]
print("original list is:",aList)
n=len(aList)
for i in range(n):
    for j in range(0,n-i-1):
        if aList[j]>aList[j+1]:
           aList [j],aList[j+1]=aList[j+1],aList[j]
print("List After Sorting :", aList)
