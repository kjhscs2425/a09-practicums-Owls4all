from utility import *
def askforstuff():
    name = ask("What is your name?")
    practicum = choose_practicum()
    print(f'Thanks, {name}, you are signed up for {practicum}.')
def choose_practicum():
    choice = ask("Which practicum do you want?\n(Costumes, Scenery, Lighting, Sound)")
    if searchList(choice,['costumes','scenery','costumes','sound','Costumes','Scenery','Lighting','Sound']):
        return choice
    else:
        print("That's not one of the options.")
        return choose_practicum()
askforstuff()