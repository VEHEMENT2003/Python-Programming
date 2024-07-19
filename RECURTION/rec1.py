# direct recursion
def compute(num):
    if(num==1):
        return 1
    else:
        return(num+compute(num-1))
# main
last=100
ans=compute(last)
print(" sum of numbers upto",last,"is =",ans)



