#import time
from colorama import Fore, Back, Style

def clear(): 
    from os import system, name 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def ending1():
    print("Deacon stays still and the guard shoots him, killing him in the process.")

def ending2():
    print("")

def ending3():
    print("")

clear()

from pyfiglet import Figlet

def GAMEOVER():
    fig = Figlet(font='graffiti')
    banner = fig.renderText("GAME OVER")

    print(banner)

print(Fore.RED + "The year is 2032 and the world has been a warzone for many many years. An enemy, whose code name is 'Ripper', who we know nothing about, has taken over. However, an organization called The Fireflies, have taken over an underground bunker. They have taken in people and have kept them safe for a long time. However, they have secrets that Deacon, a survivor, is trying to find.")
#time.sleep(10)
print(" ")
print(Style.RESET_ALL)

print("Deacon enters his room, knowing that soon he will find out once and for all what The Fireflies are hiding. He has a plan in mind.")
#time.sleep(6)
print(" ")
print("However, should he write it down or try to remember?")
# time.sleep(4)
print(" ")

choice1 = input()

if choice1 == ("write it down"):
    #time.sleep(2)
    print(" ")
    print("Deacon writes it down somewhere so he doesn't forget and tries to hide it as best as he can.")
else:
    #time.sleep(2)
    print(" ")
    print("Deacon will try to remember his plan to stay as best as he can!")

print(" ")

print("Deacon then goes to lunch where he meets up with a couple of his friends. They tell him they've been hearing rumours and that apparantely there is a safe with all sorts of info inside of it and the only way to get it is with some sort of passcode")
#time.sleep(25)
print(" ")
print("Deacon thinks about who could have the passcode and came to the conclusion that the highest ranked officer would have it and so he is now aiming to get it somehow.")
#time.sleep(15)
print(" ")

print("Should Deacon hire someone else to do the job to stay safe or should he do it himself and risk getting caught?")
print(" ")
choice2 = input("hire someone or do it himself?")

if choice2 == ("hire someone"):
    #time.sleep(3)
    print("Deacon decides to hire someone to do the job. The person hired to do the job successfully got the code to Deacon. However, they were seen by someone and a couple hours later was taken away for questioning. They didn't say a word and Deacon was grateful.")
else: 
    print("Deacon decided to attempt to get the code himself. He learned the guards schedule and knocked him out when he knew the officer would be all alone while at the same time watching out for any other officers that could be around the area.")
    #time.sleep()

#time.sleep()
print("Deacon was now close to finally finding out The Fireflies' secrets and attempting to get out of the bunker.")
#time.sleep()
print("A couple days pass and Deacon has everything planned out. He is ready to execute his plan.")
#time.sleep()

print("First, Deacon waited until the room with the safe was empty, which is only for a couple of minutes once a day. He goes inside and sees the safe in the corner of the room, he enters the code, and opens it. Inside are some keys and a folder which he takes.")
#time.sleep()
print("After that, Deacon hurries back to his room where he'll be able to read what's in the folders. He opens it.")
#time.sleep()
print("Inside there are documents with very detailed information about the Rippers. The Fireflies have apparently been sending units with scientists up to the top and they've been gathering info for a very long time. They have discovered several weaknesses however, they don't plan on using those weaknesses against the Rippers for some reason. Inside is also the location of some weapon stashes and Deacon is planning to go to these so he can protect himself at the top.")
#time.sleep()
print("Finally, Deacon is ready to escape. He grabs everything he needs and heads to the bunker door which isn't guarded because it needs keys in order to open them which very few have and the Fireflies believe the others are too scared to approach it anyway.")
#time.sleep()
print("Deacon opens the door but suddenly a guard runs in and tells him to stop while pointing a gun at him.")
#time.sleep()

choice3 = input("Do you run or stay?")

if choice3 == ("run"):
    print("Deacon decides to risk it and runs as fast as he can. This works as the guard has heard rumors about the top before and isn't gonna risk his life attempting to stop you.")
else: 
    clear()
    GAMEOVER()
    ending2()

#time.sleep()
print()