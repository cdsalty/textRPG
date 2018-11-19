

#The hero has the option to:
    # 1. Fight
    # 2. Dance
    # 3. Flee

# Go get the "OS MODULE" from Python
import os

# if you wanted to have random numbers assigned to your hero's health or power and goblin health and power, you need to add the **
# os.system() will take any linux command and if python can run it, it will.

# Get your hero's name from the player
hero_name = raw_input("What is thy name, brave adventurer? ")

def fight():
    print "Welcome %s, Thou art brave!" % hero_name
    # declare some variables
    # These variables are in the function scope meaning they are available under "fight()"
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2

    # run the game as long as both characters have health.
    while hero_health > 0 and goblin_health > 0:
        message = """You have %d health and %d power." 
        The goblin has %d health and %d power." 
        What do you want to do?
        1. fight goblin
        2. twerk
        3. flee"""
        print message % (hero_health, hero_power, goblin_health, goblin_power)
        # Get user's input
        user_input = raw_input() #it won't ask anything but it will still be waiting for the user to input some data.

        if user_input == "1":
            # The hero has decided to attack!
            # subtract goblins health by hero power
            goblin_health -= hero_power
            print "You have done %d damage to the goblin!" % hero_power
        elif user_input == "2":
            hero_health += 1
            print "The goblin stares in disbelief but breaks it down like a math teacher; Your wounds heal as the goblin twerks"
            print "Your health is now %d" % hero_health
        elif user_input == "3":
            print "Goodbye, cowardly %s" % hero_name
            # the break statement will end the loop IMMEDIATLEY!!
            break  # used to end the loop.
        else:
            # user enetered something that wasn't an allowed option.
            print "Thou art a fool. Thous has stumbledeth"

        # Now, it's the goblin's turn
        if goblin_health > 0:
            hero_health -= goblin_power
            print "The goblin hits you for %d damage" % goblin_power
            if hero_health <= 0:
                print "Thou hast been slain."
        else:
            os.system("say Hooray! thou hast killed the goblin")
            print "Horray, the goblin is gone"
        if hero_health < 5:
            print "%s has gone into a rage as death approaches. Power increased!" % hero_name 
            hero_power += 5
        raw_input("Press enter to continue")
        os.system("clear")
fight()