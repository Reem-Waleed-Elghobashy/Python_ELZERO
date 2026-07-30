# \b = back slash b 
print("Hello\b World") # will remove o

# # newline = Escape New Line + \
print("Hello \
I Love \
Python")

# Escape back slash 
print("I Love back slash \\")

# # Escape single quote = \'
print('I Love Single Quote \'Test\' ')

# # Escape Double Quote = \"
print("I Love Double Quotes \"Test\" ")

# # Line Feed = new line = \n
print("Hello World \nSecond Line")

# # \r = Cariage Return
print("123456\rAbcd")

# print("123456\rAbcde")
# \t = Horizontal tab
print("Hello\tPython")

# # \xhh = Character Hex Value
print("\x4F\x73")

#  010
# concatantion = connect two string and produce new string from two string  with +
msg="I Love"
lang="Python"
print(msg +" "+ lang)

full = msg +" "+ lang
print(full)

a="First \
Second \
Third "

b="A \
B \
C"
print(a + b)
print(a +"\n" + b)
# can not concencate string with number
# print("Hello" + 1)   #ERROR
# Can concencate string With string