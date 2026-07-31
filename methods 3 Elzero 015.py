#index(Substring, Start , End)
a="I Love Python"
print(a.index("P"))  #7
print(a.index("P",0,10))  #7
#print(a.index("P",0,5))  #Error

#find(Substring,Start , End)
b="I Love Python"
print(b.find("P")) # index number 7
print(b.find("P",0,10)) #index number 7
print(b.find("P",0,5)) #-1 بدل ما يطلع ايرور(the only difference between index() and find())

# rjust(Width, fill char) ljust(Width, fill char)
c="Reem"
print(c.rjust(10))
print(c.rjust(10,"#"))

d="Reem"
print(d.ljust(10))
print(d.ljust(10,"#"))

# splitlines()
e='''First Line
Second Line
Third Line'''
print(e)
print(e.splitlines())
print(type(e.splitlines()))

f="First Line\nSecond Line\nThird Line"
print(f.splitlines())

# expandtabs()
g="Hello\tWorld\tLove\tPython"
print(g)
print(g.expandtabs(2))
print(g.expandtabs(20))
print(g.expandtabs(1))
print(g.expandtabs(0))

one="I Love Python And 3G"
two="I Love Python And 3g"
print(one.istitle())
print(two.istitle())

three=" "
print(three.isspace())
three=""
print(three.isspace())

five="i love python"
six="I Love Python"
print(five.islower())
print(six.islower())

seven="reem_waleed"
eight="ReemWaleed100"
nine="Reem--Waleed100"
print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

x="AaaaaBbbbbb"
y="AaaaaBbbbbb111"
print(x.isalpha()) #alphabetic only from a to z
print(y.isalpha())

u="AaaaaBbbbbb"
z="AaaaaBbbbbb111"
t="11234"
print(u.isalnum()) #alphabetic or numbers 
print(z.isalnum())
print(t.isalnum())

#part4 methods
#replace(old value , new value , count) count to know how many time you can replace
a="Hello One Two Three One One"
print(a.replace("One","1"))
print(a.replace("One","1",1))
print(a.replace("One","1",2))

#join(Iterable) convert list or tuble to be string
myList=["Reem","Waleed","Elghobasghy"]
print("-".join(myList))
print(" ".join(myList))
print(", ".join(myList))
print(type("-".join(myList)))