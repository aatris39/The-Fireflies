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

clear()

print(Fore.RED + "The year is 2032 and the world has been a warzone for many many years. An organization, The Fireflies, have taken over an underground bunker. They have taken in people and have kept them same for a long time. However, they have secrets that Deacon is trying to find.")
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
    print("Deacon will try to remember his plan to stay as safe as he can!")

print(" ")

print("")