
# Strings 
myString1 = 'This is single quote '
myString2 = "This is double quote "
myString3='This is single quote "Test" '
myString4="This is double quote 'Test' "
print(myString1)
print(myString2)
print(myString3)
print(myString4)


 myString5='''First
 Second 'Test' "Test"
 Third'''

 myString6="""First
 Second "Test"  'Test' \\
 Third"""
 print(myString5)
 print(myString6)
 """
# 012

#Strings Indexing & Slicing
# All data in python is object
# object contain elements
#Every Element has its own index
# python used zero based indexing (index start from 0)
# use square brackets to access element
# Enable Accessing Parts Of Strings , Tubles Or lists

# Indexing (Acess Single item)

myString = "I Love Python"
print(myString[0])
print(myString[9])
print(myString[-1]) #First number from end
print(myString[-6]) #6th character from end

# Slicing (Access Multiple Sequence Items)
# [Start : End] End not concluded
# [Start : End : Steps]
print(myString[8:11]) #yth
print(myString[3:5]) #ov

print(myString[:10]) #if start is not here will start from 0
print(myString[5:]) #if end is not here will go to end 
print(myString[:]) #full data 

print(myString[0::1]) #full data
print(myString[::1]) #full data

print(myString[::2]) 
print(myString[::3])

#013

a="I Love Python"
b="         I Love Python"
print(len(a)) 
print(len(b)) 

# strip() بتشيل المسافات يمين و شمال 
# rstrip() بتشيل المسافات يمين بس
# lstrip() بتشيل المسافات شال بس
a="    I Love Pyhton     "
print(a.strip())
print(a.rstrip())
print(a.lstrip())
print(len(a.lstrip())) # 13 digit 5 spaces

a="#####I Love Pyhton#####"
print(a.strip("#"))
print(a.rstrip("#"))
print(a.lstrip("#"))

a="@#@#@#@#I Love Pyhton@#@#@#@#"
print(a.strip("@#"))
print(a.rstrip("@#"))
print(a.lstrip("@#"))

# title() بيحولك كل اول كلمة في النص لحرف كبير و اي كلمة بعد رقم حرف كبير 

b="I Love 2d Graphics and 3g Technology and python"
print(b.title())

#Capitalize()  وباقي الحروف صغيرة اللي في الكلمات التانية
# بتخلي كل اول حرف في الجملة ل حرف كبير
b="I Love 2d Graphics and 3g TechNology and python"
print(b.capitalize())

#zfill
c,d,e,f="1","11","111", "1111"
print(c)
print(d)
print(e)
print(f)

print(c.zfill(3))
print(d.zfill(3))
print(e.zfill(3))
print(f.zfill(3))

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

# upper()
g="reem"
print(g.upper())
# lower()
g="REEM"
print(g.lower())
