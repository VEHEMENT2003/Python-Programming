alist=[15,6,13,22,3,52,2]
print("orignal list is :",alist)
n=len(alist)
#traverse through all list elements
for i in range (n):
    #last i element are already in plce

    for j in range(0,n-i-1):
        # trverse the list from 0 to n-i-1
        # swap if the element found is greter
        #than the next element
        if alist[j] >alist[j+1]:
            alist[j],alist[j+1]=alist[j+1],alist[j]
            print ("list after sorting:",alist)
