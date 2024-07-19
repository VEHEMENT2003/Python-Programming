# binary search
def binsearch(ar,key,low,high):
    if( low>high):
      return -999
    mid=int((low+high)/2)
    if(key==ar[mid]):
     return mid
    elif(key<ar[mid]):
       high=mid-1
       return(binsearch(ar,key,low,high))
    else:
           low=mid+1
           return(binsearch(ar,key,low,high))
# main
ar=[12,13,24,25,36,37,48,49,100,222,333]
item=int(input("tell value 2 be searched"))
res=binsearch(ar,item,0,len(ar)-1)
if res>0:
                  print(item,"found at loc",res)
else:
                  print("not found")
           
