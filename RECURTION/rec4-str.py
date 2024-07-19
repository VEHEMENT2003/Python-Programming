# string reverse using recursion
def reverse(sg,n):
    if(n>0):
        print(sg[n],end=' ')
        reverse(sg,n-1)
    elif(n==0):
        print(sg[0])
s=input(" tell string")
reverse(s,len(s)-1)
    
