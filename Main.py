print("Welcome to Vyper\n\n----------\n")

AppName = "Vyper"

AppV = "1.0.0"

AppVreleasedate = "9/19/21"

while True:
    a = input("> ")
    c = a.lower()

    if c == "exit":
        exit()
    elif c == "help":
        print("Help - Shows a list of commands.\nExit - Exits Vyper\nInfo - Shows Vypers Info\nClear - Clears the console.")
    elif c == "clear":
        print("Clearing.")
        print("\n" * 180)
        print("Welcome to Vyper\n\n----------\n")
    elif c == "info":

        print("-- App Name: " + AppName + " --\n-- App Version: " +AppV+ " --\n-- App Latest Release Date: " + AppVreleasedate + " --\n")
        
            


        
    else:
        print("Unknown Command.\n")
