#methods part 2
#split() rsplit()
a="I Love Python and PHP and MySQL"
print(a.split())
print(type(a.split()))

b="I-Love-Python-and-PHP-MySQL"
print(b.split())

b="I-Love-Python-and-PHP-MySQL"
print(b.split('-'))

c="I-Love-Python-and-PHP-MySQL"
print(c.split('-',2))

d="I-Love-Python-and-PHP-MySQL"
print(d.rsplit('-',2)) #2 split start from right

c="I-Love-Python-and-PHP-MySQL"
print(c.split('-',3))

d="I-Love-Python-and-PHP-MySQL"
print(d.rsplit('-',3)) #2 split start from right

#center()
e= "Reem"
print(e.center(9)) #Spaces
print(e.center(8,"#")) # Hashes
print(e.center(14,"@"))

# Count()
f="I Love Python and PHP Because PHP is Easy"
print(f.count("PHP")) #2PHP
print(f.count("PHp"))
print(f.count("PHP",0,25)) #only1 PHP
print(f.count("PHP",0,35)) #2PHP

#swapcase() small to capital and capital to small
g="I Love Python"
h="i love PYTHON"
print(g.swapcase())
print(h.swapcase())

#startswith() The result must be boolean (True or False)
i = "I Love Python"
print(i.startswith("I"))
print(i.startswith("S"))
print(i.startswith("P",7,12))

#endswith() The result must be boolean (True or False)
j = "I Love Python"
print(j.endswith("n"))
print(j.endswith("S"))
print(j.endswith("e",2,6)) # is from 2 to 6 end with e (but the end(6) doesn't include6)