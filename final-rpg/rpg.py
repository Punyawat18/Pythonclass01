

player_name = ""
player_gender = ""

def main():
    profile_create()
    pass

def control_info():
    print("\n-----------command list-----------")
    print("status : open player status for checking and upgrade/reset ability/skill/stat")
    print("inv : open player inventory")
    print("map : open travel map for selecting location")
    print("help : showing key and command list")
    print("dif : change difficulty(easy/normal/hard/hardcore)\n")










# info and instruction
print("\n**************************************")
print("        Welcome to isekai RPG")
print("**************************************")
print("This game is text-based RPG most control will be done by text input(case insensitive) with exception of keypad_enter to use command\n")
control_info()




#profile creation
def profile_create():
    print("-------------profile creation-------------")
    player_name = input("Select a name: ")
    while True:
        print("\n", "-" * 10, "select your class(1 letter)", "-" * 10)
        player_class = input("Sage(s), Hero(h), none(n)[will lead to secret class]")
        if player_class.lower() == "s":
            player_class == "Sage"
            break
        elif player_class.lower() == "h":
            player_class == "Hero"
            break
        elif player_class.lower() == "n":
            player_class == "Demigod"
            break
        else:
            print("\ninvalid class input please enter again\n")
    print("\ndifficulty selection")
    print("easy     : enemy deal half damage while taking double damage")
    print("normal   : enemy deal and take normal damage")
    print("hard     : enemy deal double damage and take half damage")
    print("hardcore : enemy is same as hard but player only have 1 life when player die its game over")
    difficulty = input("\nSelect one [easy/normal/hard/hardcore]")


main()