

playername = "no"
playergender = "no"

def main():
    profilecreate()
    pass

def controlinfo():
    print("-----------command list-----------")
    print("status : open player status for checking and upgrade/reset ability/skill/stat")
    print("inv : open player inventory")
    print("map : open travel map for selecting location")
    print("help : showing key and command list")
    print("dif : change difficulty(easy/normal/hard/hardcor)")










# info and instruction
print("**************************************")
print("        Welcome to isekai RPG")
print("**************************************")
print("This game is text-based RPG most control will be done by text input(case insensitive) with exception of keypad_enter to use command")
controlinfo()




#profile creation
def profilecreate():
    print("-------------profile creation-------------")
    playername = input("Select a name: ")
    playergender = input("Select your gender(M/W): ")
    while playergender != "M" and playergender != "W" and playergender != "m" and playergender != "w":
        print("invalid gender please reenter")
        playergender = input("Select your gender(M/W): ")


main()