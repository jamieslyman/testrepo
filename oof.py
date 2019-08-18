inp = input ("choose a number betweem 1 and 4>")
try:
    if int(inp) == 1:
        print("rAwR sMoL bOi")
    elif int(inp) == 2:
        print("hello smol child") 
    elif int(inp) == 3:
        print("r a i n b o w s")     
    elif int(inp) == 4:
        print("wrong.")
    else:
        print("you forked up")
except ValueError:
    print("NUMBORS U HOE")