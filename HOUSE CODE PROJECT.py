#PROGRAM TO INPUT HOUSE CODE AND KNOW ABOUT YOUR HOUSE
# HERE WE ENTER HOUSE NAMES AS CODES REPRESENTED BY A DIGIT
print("Enter the following house no.s and choose the house")
print(" 1=KARVE HOUSE ") 
print(" 2=PRATAP HOUSE ")
print(" 3=SHASTRI HOUSE ")
print(" 4=TILAK HOUSE ")
print(" 5=NEHRU HOUSE ")
print(" 6=SHIVAJI HOUSE ")
x=int(input("PLEASE TELL THE HOUSE CODE YOU GOT : "))
# NOW WE ENTER OUR RESPECTIVE DIGITS 
if (x==1) :
      # ABOUT YOUR HOUSE  
      print("You are from Karve House ")    
      print("Your house is known as SPARTANS")
      print("Your House Master is Mr.N Srikarthikeyan")
      print("Your House Supdt. is Mr. D S Kunkule")
      print("So you Know about your House")
elif(x==2):
      print("You are from Pratap House ")
      print("Your house is known as EAGLES")
      print("Your House Master is Mr.S Y Patil")
      print("Your House Supdt. is Mr.S N Pawar")
      print("So you Know about your House")
elif(x==3):
      print("You are from Shastri House ")
      print("Your house is known as SHOOTERS")
      print("Your House Master is Mr.S C Thoke")
      print("Your House Supdt. is Mr.U S Babar")
      print("So you Know about your House")
elif(x==4):
      print("You are from Tilak House ")
      print("Your house is known as TIGERS")
      print("Your House Master is Mr.M Dathatri")
      print("Your House Supdt. is Mr.P D Pawar")
      print("So you Know about your House")
elif(x==5):
      print("You are from Nehru House ")
      print("Your house is known asTHUNDERS")
      print("Your House Master is Mr.Ramkrishna Yaddanpudi")
      print("Your House Matron is Mrs.N Shaikh ")
      print("So you Know about your House")
elif(x==6):
      print("You are from Shivaji House ")
      print("Your house is known as CHALLENGERS")
      print("Your House Master is Mrs.M S Kadam")
      print("Your House Supdt. is Mrs.K B Kazi")
      print("So you Know about your House")
else:
      print("Invalid House no.")       
