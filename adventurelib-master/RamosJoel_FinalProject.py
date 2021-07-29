# Final Project
#Joel 00289734 CIS 153.
#Help from book, videos the adventurelib libraby demos and instructions.
#A text adventure with a main menu.
#Finds string then turns the number portion into a floating number

print("Quest")




from adventurelib import *

import random



fhand = open('Instructions.txt')



def credits():
    print('Quest was created by Joel Ramos')
    return


def gamestart():

    print('Heres a list of commands you can do')

    Commands = {}


    for line in fhand:
        if line.startswith('C '):
            CMD = line.split()[1]



            print(CMD)



def mainmenu():
    print('1 for Game')
    print('2 for Credits')
    choice = int(input())
    return choice



result = mainmenu()
if result == 1:
    gamestart()
elif result == 2:
    credits();
else:
    print("Nope")


E = input('Hello! enter you name to start!:')

if E == ('Joel'):

    print('Hey thats my name!')

exampleList = list(E)
firstLetter = exampleList[0]

exampleList[0] = exampleList[len(exampleList) - 1]
exampleList[len(exampleList) - 1] = firstLetter

endResult = "".join(exampleList)





print("Ah yes" " " + endResult + " " "We won't be using your name but its was nice knowing")






Room.items = Bag()


current_room = starting_room = Room("""
You get outta bed, your room as that great smell of home, a gentle breeze comes from the window.
""")

odd_place = starting_room.west = Room("""
?
""")

computer = starting_room.east = Room("""
Theres a computer here, you could you use it to check some emails.
Its promting to type a password
""")

door = starting_room.north = Room("""
Theres a door in front of you, you take it and head down the stairs,
theres  a desk to your east and the door leading outside.
""")

desk = door.east = Room("""
Theres a revolver in the desk, better take it.
Monster's out there won't care if i'm armed or not,
Revolver cannot run outta ammo.
""")

outside = door.north = Room("""
You go outside, there is the remains of a fanstay land outside,
but unfournate due to the overlord they been mostly replaced with
city and more morden building building that are falling apart
""")

old_fountain = outside.west = Room("""
Theres a broken fountain, titled and with water spilling to the floor,
there use to be something here, prepahs something beautiful but now its just
a bunch of old mossy stones on the floor and junk of all kinds, cars, garbage and the sort surrounding the place.
""")


junk = old_fountain.north = Room("""
Nothing but mountains of junk, theres a old shield here,
it is dented and does not looks like it can protect much of anything
In the back of the shield is the word "destoryed"
""")


hole = outside.east = Room("""
Theres a big hole here, legends of raiders say its used to throw in any things
that don't make sense inside, then filled up after. currently its empty.
""")

Ruined_city = outside.north = Room("""
Theres a city ahead, building look old, some tilted while others have
completely fallen. Raiders can be see far off in the distant looking for anything of
worth. This was the overlords first step into mordenizing, but was abandoned.
""")



revolver = Item('revolver', 'gun')
Toaster = Item('Toaster')
old_shield = Item('old_shield', 'shield')
desk.items = Bag({revolver,})
odd_place.items = Bag({Toaster,})
junk.items = Bag({old_shield,})

inventory = Bag()


@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')

def go(direction):
    global current_room
    room = current_room.exit(direction)
    if room:
        current_room = room
        say('You go %s.' % direction)
        look()

    else:
        print('You feel like walking...., and you cant actually go that way :/')


@when('game')
def game():
    t = random.randint(0,10)

    score = 1

    for x in range(3):



        user = int(input('Guess the sercet number between 0 - 10: '))
        if user != (t):
            score += 1
        if user == (t):
            print('Oh the number was: ' + str(t))
            print(score)
            break
        elif user < 3 + (t) and user > 3 - (t):
            print('oh,very close')
        elif user > 8 + (t):
            print('Too high')
        elif user < 8 - (t):
            print('Too low')
        elif user > 9 + (t) or user < 9 - (t):
            print('Way off')

@when('take ITEM')
def take(item):
    obj = current_room.items.take(item)
    if obj:
        say('You pick up the %s.' % obj)
        inventory.add(obj)
    else:
        say('There is no %s here.' % item)


@when('drop THING')
def drop(thing):
    obj = inventory.take(thing)
    if not obj:
        say('You do not have a %s.' % thing)
    else:
        say('You drop the %s.' % obj)
        current_room.items.add(obj)


@when('look')
def look():
    say(current_room)
    if current_room.items:
        for i in current_room.items:
            say('A %s is here.' % i)


@when('inventory')
def show_inventory():
    say('You have:')
    for thing in inventory:
        say(thing)



@when('help')

def help():
    print(gamestart())



@when('destoryed')
def destoryed_order():
    say('Type calc to get different infomation for numbers you put it, type done when finished')
    say('Type power to get the power of two number')
    say('Type in game to play a game')


@when('power')
def Power():
    Num1 = int(input('Enter a Number:'))
    Num2 = int(input('Enter a number:'))




    if Num2 >= 0:
	       Power = Num1 ** Num2
	       print('The power of ' + str(Num1) + ' and ' + str(Num2) + ' is ' + str(Power))
    else:
	       print('Not supported')


@when('calc')
def calc():

    list0 = []


    while True :
        user = input('Enter a number: ')
        if user == 'done' :
            break
        try:
            Userin = float(user)
            list0.append(Userin)
        except:
            print('Invalid input')
            continue



    print ('Greatest Number: ' + str(max(list0)))
    print ('Least Number: ' + str(min(list0)))
    print ('Sum of the numbers: ' + str(sum(list0)))
    print ('How many numbers added: ' + str(len(list0)))
    avg = sum(list0) / len(list0)
    print('This is the avg: ' + str(avg))



@when('quit')
def quit():
    close()





look()
start()
