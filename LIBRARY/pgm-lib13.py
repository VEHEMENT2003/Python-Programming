# pgm for encription and decription using standard string functions
def encr(str,ekey):
  return ekey.join(str)
def decr(str,ekey):
    return ekey.split(str)
str="india"
ekey="+"
print(encr(str,ekey))
print(decr(str,ekey))
a1=encr(str,ekey)
a2=decr(a1,ekey)
a3=" ".join(a2)
print(a1)
print(a2)
print(a3)
