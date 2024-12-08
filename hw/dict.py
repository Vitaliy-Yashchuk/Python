users = {}

while True:
    print("Add new user: \t\t\t\tpress 1")
    print("Delete user: \t\t\t\tpress 2")
    print("Change password: \t\t\tpress 3")
    print("Check password: \t\t\tpress 4")
    print("Get password information by user login: press 5")
    print("Exit: \t\t\t\t\tpress 0")

    choise = input()
    
    match choise:
        case "1":
            login = input("Enter your login: ")
            password = input("Enter your password: ")
            if login in users:
                print("User already exists!!!")
            else:
                users[login] = password
                print(f"User {login} added successfully.")
        case "2":
            login = input("Enter your login: ")
            if login in users:
                del users[login]
                print(f"User {login} deleted successfully.")
            else:
                print("Not founded")
        case "3":
            login = input("Enter your login: ")
            password = input("Enter your new password: ")
            if login in users:
                if users[login] != password:
                    users[login] = password
                    print("Password has been changed")
                else:
                    print("The new password cannot be the same as the old one")
            else:
                print("Login not found. Please check your login.")
        case "4":
            for i in users.values():
                print(i)
        case "5":
            login = input("Enter your login: ")
            if login in users:
                print(f"Your password is {users[login]}")
            else:
                print("Wrong login")
        case "0":
            print("Exiting the program.")
            break  
        case _:
            print("Invalid choice. Please try again.")
    print(users)

