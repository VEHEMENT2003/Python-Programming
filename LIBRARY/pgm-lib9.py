# same var  name in module and pgm
# pgm var  takes prefrence over module var
# here var x   is  in lib4 and pgm also
# but x declared b4 importing 
x=100
from lib4 import *
# x=100
print(x)
# def india():
#    print(" india is my country")
india()
