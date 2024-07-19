lst = eval (input("enter list :"))
length = len(lst)
end = lenght-1
print("orignal list : ",lst)
i = 0
aawhile (i <= end):
    ele =lst[i]
    if ele == 0:
        for j in range(i, end):
            lst[j] = lst[j+1]
        else:
                lst[end] = 0
                end -= 1
                if lst[i] !=0:
                    i+=1
                    print("zero shifted :",
