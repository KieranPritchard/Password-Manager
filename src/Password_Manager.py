from cryptography.fernet import Fernet
import hashlib
import sys
import os

# Loads the key at the start of the program.
def load_key():
    # Contains key path containing key
    key_path = "Password_Manager/res/key.key"

    # Returns boolean value when checking if file exists
    file_exists = os.path.isfile(key_path)

    # Checks if file_exists variable is true, if not it generates and reads a new key.
    if file_exists:
        try:
            with open(key_path, "rb") as key_file:
                key = key_file.read()
            return key
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        new_key = Fernet.generate_key()

        try:
            with open(key_path, "wb") as key_file:
                key_file.write(new_key)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        return new_key  # Return the newly generated key directly

# Login function.
def login():
    # Hashes for login.
    username = "username"
    password = "password"

    try:
        # Converts username to a hash.
        username_login_input = input("Please input username: ").encode()
        username_login_hash = hashlib.sha256(username_login_input).digest()

        # Converts password to a hash.
        password_login_input = input("Please input password: ").encode()
        password_login_hash = hashlib.sha256(password_login_input).digest()
        
        # Checks if the hashes match up
        if username == username_login_hash and password == password_login_hash:
            print("-" * 30)
            print("Login Successful!")
            return True
        else:
            print("-" * 30)
            print("Invalid Login, username and/or password incorrect.")
            return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Adds credentials.
def add_credentials(cipher=Fernet(load_key())):
    # Credentials to add.
    username_to_add = input('Please input username: ')
    password_to_add = input('Please input password: ')
    service_to_add = input('Please input service: ')

    # Encrypts user inputs to be written into a text file.
    plaintext_credentials = f'Service: {service_to_add.capitalize()} Username: {username_to_add}, Password: {password_to_add}.'
    ciphertext_credentials = cipher.encrypt(plaintext_credentials.encode())

    # Writes them to a file.
    try:
        with open("Password_Manager/res/Password Database.txt", "a") as file:
            file.write(ciphertext_credentials.decode() + '\n')
    except Exception as e:
        print(f"Error encountered when adding user credentials: {e}")

# Reads user-added credentials.
def read_credentials(cipher=Fernet(load_key())):
    # Array where credentials are added to.
    credentials = []
    
    try:
        # Opens file then iterates through each of the lines, decrypting and adding to a list as it goes.    
        with open("Password_Manager/res/Password Database.txt", "r") as file:
            for x in file:
                decrypted_line = cipher.decrypt(x).decode()
                credentials.append(decrypted_line)

        # Prints the array of credentials
        for x in credentials:
            print(x)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Edits credentials previously added by the user
def edit_credentials(cipher=Fernet(load_key())):
    # Takes input from the user
    service_to_edit = input("Please input the service you want to edit: ")
    edited_username = input("Please input the new username: ")
    edited_password = input("Please input the new password: ")
    
    # Array where credentials are added to.
    credentials = []

    try:
        # Opens the file then loops through it to find the credentials that need editing
        with open("Password_Manager/res/Password Database.txt", "r") as file:
            for x in file:
                decrypted_line = cipher.decrypt(x).decode()
                if service_to_edit.capitalize() in decrypted_line:
                    decrypted_line = f'Service: {service_to_edit.capitalize()} Username: {edited_username}, Password: {edited_password}.'
                credentials.append(decrypted_line)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    try:
        # Writes the updated arrays to the file.
        with open("Password_Manager/res/Password Database.txt", "w") as file:
            for x in credentials:
                encrypted_line = cipher.encrypt(x.encode())
                file.write(encrypted_line.decode() + '\n')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Removes user-added credentials
def remove_credentials(cipher=Fernet(load_key())):
    # Asks the user for which service and its credentials to remove.
    service_to_remove = input("Please input the service you want to remove: ")
    
    # Array where credentials are added to.
    credentials = []
    
    try:
        # Opens the text file with credentials, it then loops through the list
        with open("Password_Manager/res/Password Database.txt", "r") as file:
            for x in file:
                decrypted_line = cipher.decrypt(x).decode()

                # Adds credentials that aren't the ones to remove
                if service_to_remove.capitalize() not in decrypted_line:
                    credentials.append(decrypted_line)

        # Writes the remaining credentials to the credentials file
        with open("Password_Manager/res/Password Database.txt", "w") as file:
            for x in credentials:
                encrypted_line = cipher.encrypt(x.encode())
                file.write(encrypted_line.decode() + '\n')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# The manager's menu
def menu():
    print("-" * 30)
    print("(1) - Add Credentials\n(2) - Read Credentials\n(3) - Edit Credentials\n(4) - Remove Credentials\n(5) - Exit")
    print("-" * 30)

    try:
        # Asks the user for what option they want
        user_selection = int(input("Please Select Option: "))

        # Checks what function to use based on users selection
        if user_selection == 1:
            add_credentials()
        elif user_selection == 2:
            read_credentials()
        elif user_selection == 3:
            edit_credentials()
        elif user_selection == 4:
            remove_credentials()
        elif user_selection == 5:
            sys.exit()
        else:
            print("Invalid Input")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Header for the program
    print("-" * 30)
    print("Password Manager")
    print("-" * 30)
    
    # Calls the login function
    login()
    
    # Checks the login was successful, if so it runs the rest of the program like normal.
    while True:
        menu()

if __name__ == "__main__":
    main()
