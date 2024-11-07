import csv


##file path
csv_file = 'C:\\Users\\sora\\Documents\\GitHub\\Pythonclass01\\final-project\\passproject\\password_data.csv'


##main function
def main():
    while True:
        mode = operation_mode()
        if mode == "view":
            user_app_name = input("Name of app you want password of, All if you wish for every password stored: ")
            view_password(user_app_name)
        elif mode == "add":
            user_app_name = input("name for the app: ")
            user_username = input("Username: ")
            user_password = input("Password: ")
            store_in_csv(user_app_name, user_username, user_password)
        elif mode == "remove":
            user_app_name = input("name for the app you wish to remove, All if you wish to delete everything: ")
            user_username = input("Username that you wish to remove from app, All for every password related to this app: ")
            remove_from_csv(user_app_name, user_username)


## write in csv(havent tested no problem yet)
def store_in_csv(app: str, username: str, password: str) -> None:
    """
    This function is use to store password in csv file\n
    app -> app name for the password\n
    username -> username for password in this app\n
    password -> password to stored   
    """
    encrypted_password = encryption(password)
    with open(csv_file, mode="a", newline="\n") as file:
        writer = csv.writer(file)
        writer.writerow([app, username, encrypted_password])
        print("Successfully added to password manager for\napp: ", app, 
              "\nusername: ", username, 
              "\npassword: ", password)


##remove from csv(tested)
def remove_from_csv(app: str, username: str) -> None:
    """
    This function is for remove password stored in csv file\n
    app -> app that want to delete with All being delete everything\n
    username -> remove this username from selected app with All being delete every username from selected app
    """
    ##read csv into list for rewriting
    with open(csv_file, mode="r") as file:
        password_data = csv.DictReader(file)
        temp_data = list(password_data)

    ##open file in write mode for rewriting
    with open(csv_file, mode="w+", newline="\n") as file:
        writer = csv.writer(file)
        writer.writerow(["app", "username", "password"])

        ##remove all
        if app == "All":
            print("remove all password stored")

        ##remove specific app
        else:
            ##remove all username of the app
            if username == "All":
                for element in temp_data:
                    if element["app"] != app:
                        writer.writerow([element["app"], 
                                         element["username"], 
                                         element["password"]])
                print("remove all password from: ", app)
            else:
                ##remove specific username from specific app
                for element in temp_data:
                    if (element["app"] == app) and\
                          (element["username"] == username):
                        continue
                    writer.writerow([element["app"],
                                     element["username"],
                                     element["password"]])
                print("remove password from\napp: ", app, 
                      "\nusername: ", username)


## take input from user for mode of operation (add,remove,view,stop)
##Havent tested yet
def operation_mode() -> str:
    """
    This function is for asking user the mode of the program with input of\n
    add -> add new password to csv\n
    remove -> remove password from csv\n
    view -> view the password in csv\n
    stop -> stop the program
    """
    print("add(add new password to manager), remove(remove the password), stop(terminate the program), view(view stored password)")
    user_status = input("action(case sensitive): stop,add,remove,view: ")
    while (user_status != "add") and (user_status != "stop")\
          and (user_status != "view") and (user_status != "remove"):
        print("invalid input please enter again")
        user_status = input("action(case sensitive): stop,remove,add,view: ")
    if user_status == "stop":
        print("Stop the program")
        exit(0)
    else:
        return user_status
    

##view password
##havent tested yet 
def view_password(app_name: str) -> None:
    """
    This function is for viewing password\n
    app_name -> The name of app user want to view password stored in with All being everything stored in csv\n
    """
    with open(csv_file, mode="r") as file:
        temp_data = csv.DictReader(file)
        raw_data = list(temp_data)
        password_data = []
        for raw in raw_data:
            raw["password"] = decryption(raw["password"])
            password_data.append(raw)
        length_of_data = 0
        if app_name == "All":
            for row in password_data:
                print(row)
                length_of_data += 1
        else:
            for row in password_data:
                if row["app"] == app_name:
                    print(row)
                    length_of_data += 1
        if length_of_data == 0:
            print("There is no password for app user input")
            return
        else:
            return
        
    
def encryption(password: str) -> str:
    encrypted = "".join(reversed(password))
    return encrypted


def decryption(password: str) -> str:
    decrypted = "".join(reversed(password))
    return decrypted


main()