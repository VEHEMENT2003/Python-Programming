def Bsearch(AR,ITEM):
    beg = 0
    last = len(AR) - 1
    while (beg<= last):
        mid = (beg + last)/2 
        if (ITEM == AR[mid]):
            return mid
        elif(ITEM >AR[mid]):
            beg=mid +1
        else:
                last = mid-1
    else:
        return False


#main........................................................................................
myList = [10,20,30,40,50,50,60,70]
print("the list inserted order is ")
print (myList)
ITEM = int(input("Enter element to be deleted:\n"))

position= Bsearch(myList,ITEM)
if position:
    del myList [position]
    print("the list after deleting",ITEM,"is")
    print(myList)
else:
    print("SORRY! no such element is in the list")
        
