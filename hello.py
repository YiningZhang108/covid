print ("hello world")


#name = input("best country in the world: ")
#print (name)

'''
if (name.lower() == "canada"):
    print(name + " is the best country")
elif (name == "italy"):
    print(name.lower() + " is the second best country")
else:
    print ("incorrect answer")
'''

fruits = ['apple,grannysmith,gala', 'peach,sweet,sour', 'orange,manderin,bloodorange', 'bananas,big,small']
for fruit in fruits:
    templist = fruit.split(",")
    print(fruit)
    print(templist)
