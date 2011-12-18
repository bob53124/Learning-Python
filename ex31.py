print """
This is a short adventure game created by Robert Greener.
in this game n is north e is east s is south and w is west.
You can exit by typing exit at the prompt

-----------------------------------------------------------
"""
def part1():
    print "You enter a dark room with two doors. Do you go through the door to the east or door to the west?"
    
    door = raw_input("> ")
    
    if door == "e":
        part2()
    elif door == "w":
        part3()
    elif door == "exit":
        exit()
    else:
        print "Doing %s was pointless. Try Again" % door   

def part2():
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    print "There are doors to the east and west"
    
    bear = raw_input("> ")
        
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    elif bear == "w":
        part1()
    elif bear == "e":
        part5()
    elif door == "exit":
        exit()
    else:
        print "Well, doing %s is pointless. Try Again." % bear
        part2()

def part3():
    print "You stare into the endless abyss at Cthuhlu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    print "The only door is to the east"
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
        part3()
    elif insanity == "e":
        part1()
    elif insanity == "3":
        print "Your Crazy"
        part3()
    elif door == "exit":
        exit()
    else:
        print "Doing %s is pointless. Try Again" % insanity
        part3()

def part5():
    print "You are in a corridor nothing of intrest appears to be here."
    print "Doors lead east and west"

def exit()
    print "Goodbye."

part1()
