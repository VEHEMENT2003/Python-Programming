alist=[6,13,22,3,52,2,45,34,67,87,90,123,45667,45,]
print("orignal list is :",alist)
for i in range(1,len(alist)):
    key =alist[i]
    j = i-1
    while j >=0 and key < alist[j] :
        alist [j+1]=alist[j]                    #shift element to right to make room for key
        j = j-1
else:
    alist [j+1]=key
print ("list after sorting :",alist)
