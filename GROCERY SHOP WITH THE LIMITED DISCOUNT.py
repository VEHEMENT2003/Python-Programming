#PROGRAMME NO - 
#PROGRAMME TO FOR GROCERY SHOPS FOR BILLING WITH DISCOUNT
print("!!!!WELCOME TO MY SSS GROCERY SHOP!!!!")
print("sugarcost=40.20/kg,biscuitcost=10.78/packet,pulsescost=60.62/kg")
sugarquantity=int(input("please tell the quantity of sugar="))
biscuitquantity=int(input("please tell the quantity of biscuits="))
pulsesquantity=int(input("please tell the quantity of pulses="))
totalcostofsugar=sugarquantity*40.20
toatalcostofbiscuit=biscuitquantity*10.78
totalcostofpulsesquantity=pulsesquantity*60.62
TOTALBILL=totalcostofsugar+toatalcostofbiscuit+totalcostofpulsesquantity
if((TOTALBILL>=1000)and(TOTALBILL<=1499)):
    print("CONGO YOU HAVE SHOPPED ABOVE Rs.1000 ")
    print("YOU WILL HAVE 5% DISCOUNT")
    A=5/100*TOTALBILL
    TOTALBILLS=TOTALBILL-A
    print("YOUR ORIGINAL BILL WAS = ",TOTALBILL)
    print("THE DISCOUNT YOU RECIEVED IS = ",A)
    print("HENCE YOUR BILL IS = ",TOTALBILLS)
    print("...THANKS FOR COMING...")
    print("!!!!VISIT AGAIN!!!!")
    print(input("ARE YOU HAPPY WITH OUR SERVICE="))
if(TOTALBILL>=1500)and(TOTALBILL<=1999):
    print("CONGO YOU HAVE SHOPPED ABOVE Rs.1500 ")
    print("YOU WILL HAVE 10% DISCOUNT")
    E=10/100*TOTALBILL
    TOTALBILLS=TOTALBILL-E
    print("YOUR ORIGINAL BILL WAS = ",TOTALBILL)
    print("THE DISCOUNT YOU RECIEVED IS = ",E)
    print("HENCE YOUR BILL IS = ",TOTALBILLS)
    print("...THANKS FOR COMING...")
    print("!!!!VISIT AGAIN!!!!")
    print(input("ARE YOU HAPPY WITH OUR SERVICE="))
if(TOTALBILL>=2000)and(TOTALBILL<=2999):
    print("CONGO YOU HAVE SHOPPED ABOVE Rs.2000 ")
    print("YOU WILL HAVE 15% DISCOUNT")
    D=15/100*TOTALBILL
    TOTALBILLS=TOTALBILL-D
    print("YOUR ORIGINAL BILL WAS = ",TOTALBILL)
    print("THE DISCOUNT YOU RECIEVED IS = ",D)
    print("HENCE YOUR BILL IS = ",TOTALBILLS)
    print("...THANKS FOR COMING...")
    print("!!!!VISIT AGAIN!!!!")
    print(input("ARE YOU HAPPY WITH OUR SERVICE="))
if(TOTALBILL>=3000)and(TOTALBILL<=3999):
    print("CONGO YOU HAVE SHOPPED ABOVE Rs.3000 ")
    print("YOU WILL HAVE 20% DISCOUNT")
    C=20/100*TOTALBILL
    TOTALBILLS=TOTALBILL-C
    print("YOUR ORIGINAL BILL WAS = ",TOTALBILL)
    print("THE DISCOUNT YOU RECIEVED IS = ",C)
    print("HENCE YOUR BILL IS = ",TOTALBILLS)
    print("...THANKS FOR COMING...")
    print("!!!!VISIT AGAIN!!!!")
    print(input("ARE YOU HAPPY WITH OUR SERVICE="))
if(TOTALBILL>=4000):
    print("CONGO YOU HAVE SHOPPED ABOVE Rs.4000 ")
    print("YOU WILL HAVE 30% DISCOUNT")
    B=30/100*TOTALBILL
    TOTALBILLS=TOTALBILL-B
    print("YOUR ORIGINAL BILL WAS = ",TOTALBILL)
    print("THE DISCOUNT YOU RECIEVED IS = ",B)
    print("HENCE YOUR BILL IS = ",TOTALBILLS)
    print(input("ARE YOU HAPPY WITH OUR SERVICE="))
    print("...THANKS FOR COMING...")
    print("!!!!VISIT AGAIN!!!!")
else:
    print("...THANKS FOR COMING...")
    print("!!!!VISIT AGAIN!!!!")


