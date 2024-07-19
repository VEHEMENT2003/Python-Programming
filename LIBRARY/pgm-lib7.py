# same variabe name in module and pgm
# pgm variable takes prefrence over module variable
# here x is 20 in lib3
from lib3 import *
# x=100
print(x)
