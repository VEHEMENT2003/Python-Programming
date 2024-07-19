import bisect
myself = [10,20,30,40,50,60,70]
print("the list in sorted order is ")
print(mylist)
ITEM = int(input("enter new element to be inserted:"))

ind = bisect.bisect(mylist,ITEM)
bisect.insort(mylist,ITEM)

print(ITEM, "inseted at index", ind)
print("the list after  inserting new element is")
print(mylist)
