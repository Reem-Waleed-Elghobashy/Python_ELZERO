# List Items Are Enclosed in square Brackets
# List are ordered, to use index to access Item
# list are Mutable can add delete edit
# list items is not unique
# list can have different data types
myList=["One","Two","One",1,100.5,True]
print(myList) #Whole list
print(myList[1]) #Two
print(type(myList[1])) # string
print(myList[-1]) #True
print(myList[-3]) #1
print(myList[1:4]) #Two One 1
print(myList[:4]) # ["One","Two","One",1]
print(myList[1:]) # ["Two","One",1,100.5,True]
print(myList[::1]) #Whole list
print(myList[::2]) # ['One', 'One', 100.5]

myList=["One","Two","One",1,100.5,True]
print(myList)
myList[1] = 2
myList[-1] = False
print(myList)
myList=["One","Two","One",1,100.5,True]
myList[0:2]=[] 
print(myList)
myList=["One","Two","One",1,100.5,True]
myList[0:3]=["R","E","M"]
print(myList)
myList=["One","Two","One",1,100.5,True]
myList[0:3]=["R"] #edit not replace
print(myList)


#022 methods of list
# append()
MyFriends=["Reem","Sara","Jana"]
myOldFriends=["omar","ali","sameh"]
MyFriends.append("hana")
MyFriends.append(100)
MyFriends.append(150.200)
MyFriends.append(True)
MyFriends.append(myOldFriends)
print(MyFriends)
print(MyFriends[2])
print(MyFriends[6])
print(MyFriends[7])
print(MyFriends[7][2])

# extend()
a=[1,2,3,4]
b=["A","B","C"]
c=["One","Two"]
a.extend(b)
a.extend(c)
print(a)

# remove()
x=[1,2,3,4,5,"Osama",True,"Osama","Osama"]
x.remove("Osama")
print(x)

# sort() can not arrange integer with string (integer only or string only)
y=[1,2,100,120,-10,17,29]  
y.sort()
print(y)
y.sort(reverse=True) # arrange then reverse
print(y)
y=["Z","a","A","c"]
y.sort() # CAPITAL FIRST
print(y)
y=["a","z","c"]
y.sort(reverse=True)
print(y)

# reverse() reverse list only without sorted it
z=[10,1,9,80,100,"Osama",100]
z.reverse()
print(z)

#methods part 2
a=[1,2,3,4]
a.clear()
print(a)

#copy()
b=[1,2,3,4]
c=b.copy()
print(b)
print(c)

b.append(5)
print(b)
print(c)

# count()
d=[1,2,3,4,3,9,10,1,2,1]
print(d.count(1))

#index()
e=["Osama","Ahmed","Sayed","Ramy","Ahmed","Ramy"]
print(e.index("Ramy")) #first index it see

# insert() هيحط ال انت هتديهوله قبل ال index (you give it)
f=[1,2,3,4,5,"A","B"]
f.insert(0,"Test")
f.insert(-1,"Test")
print(f)

# pop()
g=[1,2,3,4,5,"A","B"]
print(g.pop(2))
print(g)
g=[1,2,3,4,5,"A","B"]
print(g.pop(-1))
print(g)
g=[1,2,3,4,5,"A","B"]
print(g.pop(-3))
print(g)