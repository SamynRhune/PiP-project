from CommandoHandler import CommandoHandler

handler = CommandoHandler()

print("\n\nHet programma wordt opgestart ...\n\n")
user_input = ""
while( user_input != "EXIT"):
    user_input = input("Geef een commando in? Typ HELP om alle commando's te krijgen: \n").upper()
    handler.inputCommand(user_input)






