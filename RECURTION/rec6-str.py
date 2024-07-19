# string reverse using recursion
def reverse(sg,n):
    if(n>0):
        k=len(sg)-n
        reverse(sg,n-1)
        print(sg[k],end=' ')
    elif(n==0):
        return
s=input(" tell string")
reverse(s,len(s)-1)
    
