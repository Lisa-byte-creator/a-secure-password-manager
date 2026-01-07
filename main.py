from app.database import create_tables
from app.auth import save_master_password, verify_master_password
from app.password_checker import add_password, get_passwords

#maximum attempts of login before app locks
MAX_ATTEMPTS = 3


def setup_master_password():

    #prompts the user to create a new and save masterpassword 
    password = input("Create master password: ")
    save_master_password(password)
    print("Master password saved securely.")


def login():

    #handling user login attempts and verifying the master paswword
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        password = input("Enter master password: ")

        if verify_master_password(password):
            print("Login successful.")
            return password
        else:
            attempts += 1
            remaining = MAX_ATTEMPTS - attempts
            print(f"Invalid password. Attempts remaining: {remaining}")

    print("Too many failed attempts. Application locked.")
    return None


def menu(master_password):

    #displaying the menu
    while True:
        print("\n1. Add password")
        print("2. View passwords")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            service = input("Service: ")
            username = input("Username: ")
            password = input("Password: ")

            try:
                #saving the password entered
                add_password(service, username, password, master_password)
                print("Password stored securely.")
                #handling errors for example if decryption fails
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            #retrieve nd decrypt all saved passwords
            passwords = get_passwords(master_password)

            if not passwords:
                print("\nNo passwords stored yet.")
            else:
                print("\nSaved passwords:")
                for service, username, password in passwords:
                    print(f"Service: {service}")
                    print(f"Username: {username}")
                    print(f"Password: {password}")
                    print("-" * 20)

        elif choice == "3":
            #break the loop and exit the program
            break

        else:
            print("Invalid choice. Try again.")

#entry point of the program
if __name__ == "__main__":
    #ensures database tables exist before executing
    create_tables()

    #log in options
    print("1. Setup master password")
    print("2. Login")

    option = input("Choose: ")

    if option == "1":
        #  create a new master password
        setup_master_password()
    elif option == "2":
        # Attempt to log in with existing master password
        master = login()
        if master:
            # Launch main menu if login was successful
            menu(master)
    # No action for invalid initial choice — program ends
