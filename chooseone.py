inp = input("Choose a number between 1 and 3>")
try:
    if int(inp) == 1:
        print("He-Hewwo???")
    elif int(inp) == 2:
        print("OwO What's this???")
    elif int(inp) == 3:
        print("THAT'S THE WRONG NUMBUH! OHHHHHH")
    else:
        print("Invalid input, try again (rerun)")
except ValueError:
    print("Please type a number instead")