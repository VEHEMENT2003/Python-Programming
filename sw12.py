#string analyising
strl=input("plz tell string")
digit=alpha=0
others=0
for x in strl :
        if(x. isdigit ()):
            digit=digit+1
        elif(x. isalpha()):
            alpha=alpha+1
        elif(not(x.isalpha())and not(x. isdigit())):
            others=others+1
print("the num of digit=",others)

        

