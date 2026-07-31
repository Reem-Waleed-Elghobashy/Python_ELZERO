# %s place holder (s for string), %d place holder (d for digit), %f place holder for float
name="Reem"
age=19
rank=10
print("My Name is:"+name)
#print("My Name is :"+name+" and My Age is:" +age)#Error can not concencate string with int
print("My Name is: %s" % "Reem")
print("My Name is: %s" % name)
print("My Name is: %s and My Age is: %d"%(name,age))
print("My Name is: %s and My Age is: %d and My Ran is: %f"%(name,age,rank))

n="Reem"
l="Python"
y=10
print("My Name is %s I am %s Developer with %d  Years experience"%(n,l,y))

#control floating point number
myNumber=10
print("My Number is: %d" %myNumber)
print("My Number is: %f" %myNumber)
print("My Number is: %.2f" %myNumber)

#Trancate String
myLongString="Hello Peoples of Elzero School I Love You All"
print("Message is %s"%myLongString)
print("Message is %.5s"%myLongString) #first 5 elements(Hello only)

#new way formatting 018
print("My Name is: {}".format("Reem"))
print("My Name is: {}".format(name))
print("My Name is: {} and My Age is: {}".format(name,age))
print("My Name is: {:s} and My Age is: {:d} and My Ran is: {:f}".format(name,age,rank))
#{:s} for string , {:d} for number ,{:f} for floating

n="Reem"
l="Python"
y=10
print("My Name is {} I am {} Developer with {}  Years experience".format(n,l,y))

#control floating point number
myNumber=10
print("My Number is: {:d}" .format(myNumber))
print("My Number is: {:f}" .format(myNumber))
print("My Number is: {:.2f}" .format(myNumber))

#Trancate String
myLongString="Hello Peoples of Elzero School I Love You All"
print("Message is {:s}".format(myLongString))
print("Message is {:.5s}".format(myLongString)) #first 5 elements(Hello only)
print("Message is {:.13s}".format(myLongString)) #first 13 elements(Hello Peoples)

#format money
myMoney=500162350198
print("My Money in Bank Is: {}".format(myMoney))
print("My Money in Bank Is: {:_}".format(myMoney)) # after every 3 numbers will put underscore
print("My Money in Bank Is: {:_d}".format(myMoney)) # after every 3 numbers will put underscore
print("My Money in Bank Is: {:,d}".format(myMoney)) # after every 3 numbers will put comma
#print("My Money in Bank Is: {:&d}".format(myMoney)) #Error not all characters can use

# Rearrange Items
a,b,c="One","Two","Three"
print("Helo {} {} {}".format(a,b,c)) 
print("Helo {1} {2} {0}".format(a,b,c))
print("Helo {2} {0} {1}".format(a,b,c))

x,y,z=10,20,30
print("Helo {} {} {}".format(x,y,z)) 
print("Helo {1} {2} {0}".format(x,y,z)) 
print("Helo {2} {0} {1}".format(x,y,z)) 

x,y,z=10,20,30
print("Helo {} {} {}".format(x,y,z)) 
print("Helo {1:d} {2:d} {0:d}".format(x,y,z)) 
print("Helo {2:f} {0:f} {1:f}".format(x,y,z)) 
print("Helo {2:.2f} {0:.4f} {1:.5f}".format(x,y,z))

# Format in version 3.6+
myName="Reem"
myAge=19
print("My Name is :{myName} and My Age is :{myAge}")
print(f"My Name is :{myName} and My Age is :{myAge}")
#website important (PyFormat.info)