# linear search
def Lsearch(AR, ITEM) :
    i=0
    while i < len(AR) and AR[i] != ITEM :
        i += 1
    if i < len (AR) :
        return i
    else :
        return false
#main.....................................
N = int(input("enter desired linear-list size(max.50)..."))
print("\nenter elements for linear list\n")
AR = [0]*N                           # initialize list of size N with zeros
for i in range(N) :
    AR[i] = int(input("element" + str(i)+":"))

ITEM = int(input("\nEnter to be searchedfor ..."))
index =Lsearch (AR, ITEM)

if index :
    print("\n element found at index :", ",position :",(index +1))
else:
    print("\nsorry!!!!!! given element could not be found .\n")
    
        
