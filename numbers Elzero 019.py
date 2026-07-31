#integer + or - or 0
print(type(1))
print(type(100))
print(type(10))
print(type(-10))
print(type(-110))
# Float
print(type(1.500))
print(type(100.99))
print(type(-10.99))
print(type(0.99))
print(type(-0.99))
#Complex number
myComplex =5+6j # real part and imaginary part
print(type(myComplex)) 
print("Real Part Is {}".format(myComplex))
print("Real Part Is {}".format(myComplex.real))
print("Imaginary Part Is {}".format(myComplex.imag))

#[1] You Convert From Int to Float or Complex
#[2] You Convert From float To Int or Complex
#[3] You Cannot Convert Complex To Any Type
print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))

print(10+9j)
#print(int(10+9j)) #Error

#020 Arithmetic Operators
#Addition
print(10+30)
print(-10+20)
print(1+ 2.66)
print(1.2+1.2)
#Subtraction
print(60-30)
print(-30-20)
print(-30- -20)
print(5.66-3.44)
#Multiplication
print(10*3)
print(5+10*100)
print((5+10)*100)
#Division
print(100/20)
print(int(100/20))
#Modules %
print(8%2)
print(9%2)
print(20%5)
print(22%5)
#Exponent
print(2**5) # 2 power 5
print(2*2*2*2*2)
print(5**4)
print(5*5*5*5)
#Floor Division the the result is int only
print(100//20)
print(110//20)
print(119//20)
print(120//20)
print(130//20)
print(139//20)
print(140//20)