print("Welcome to Grocery Shop")
QSugar=int(input("tell me the quantity of Sugar"))
QBiscuit=int(input("tell me the quantity of Biscuit"))
QPulse=int(input("tell me the quantity of Pulse"))
Sugar=40
Biscuit=10
Pulse=60
sugar=Sugar*QSugar
biscuit=Biscuit*QBiscuit
pulse=Pulse*QPulse
Bill=sugar+biscuit+pulse
print("Sugar=",sugar,"Rs")
print("biscuit=",biscuit,"Rs")
print("pulse=",pulse,"Rs")
print("TotalBill=",Bill,"Rs")

discount=Bill*15/100
print("totalbill =",discout,"rs")

