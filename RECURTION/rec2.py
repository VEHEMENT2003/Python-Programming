# direct recursion same example two steps
def compute(num):
    if(num==1):
        return 1
    else:
        p=compute(num-1)
        print("p =",p)
        return(num+p)
last=6
ans=compute(last)
print(" sum of numbers upto",last,"is =",ans)
