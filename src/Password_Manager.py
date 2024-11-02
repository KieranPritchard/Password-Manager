from cryptography.fernet import Fernet
import hashlib
import sys
import os

# Loads the key at the start of the programe.
def load_key():
    
    # Contains key path containing key
    key_path = "Python/Projects/Password-Manager/res"

    # Returns boolean value when checking if file exists
    file_exists = os.path.isfile(key_path)

    # Checks if file_exists varible is true, if not it generates and reads a new key.
    if file_exists == True:
        try:
            with open("Python/Projects/Password Manager/key.key", "rb") as key_file:
                key = key_file.read()
            return key
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        new_key = Fernet.generate_key()

        try:
            with open("Python/Projects/Password Manager/key.key","wb") as key_file:
                key_file.write(new_key)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        try:
            with open(key_path, "rb") as key_file:
                key = key_file.read()
            return key
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Login function.
def login():
    
    #Hashes for login.
    username = b's!\x9e\xb4J\xa1\x88\xef\x87\xc1\xcb]\xa1\x1f}\x0e\xd8orx\xbe\xcd\x1f\xe1i\x99\xf6\xfa_\x15A\xbd'
    password = b'\xc3\x0e\x0evi\xa0i\x04\xd1D\xd4J\x7f\xa7\xef\xa4\x1e\xb4#:(\xf0`AZ\xd0\x1b/^\x97g\xc1'

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
def add_credentials(cipher = Fernet(load_key())):

    # Credentials to add.
    username_to_add = input('Please input username: ')
    password_to_add = input('Please input password: ')
    service_to_add = input('Please input service: ')

    # Encrypts user inputs to be written into a text file.
    plaintext_credentials = f'Service: {service_to_add.capitalize()} Username: {username_to_add}, Password: {password_to_add}.'
    ciphertext_credentials = cipher.encrypt(plaintext_credentials.encode())

    # Writes them to a file.
    try:
        with open("Python/Projects/Password Manager/Password Database.txt", "a") as file:
            file.write(ciphertext_credentials.decode() + '\n')
    except:
        print("Error encountered when adding user credentials.")

# Reads user-added credentials.
def read_credentials(cipher = Fernet(load_key())):
    
    # Array where credentials are added to.
    credentials = []
    
    try:
        # Opens file then iterates though each of the lines, decrypting and adding to a list as it goes.    
        with open("Python/Projects/Password Manager/Password Database.txt", "r") as file:
                for x in file:
                    decrypted_line = cipher.decrypt(x).decode()
                    credentials.append(decrypted_line)

                # Prints the the array of credentials
                for x in credentials:
                    print(x)
    except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Edits credentials previously added by the user
def edit_credentials(cipher = Fernet(load_key())):

    # Takes input from the user
    service_to_edit = input()
    edited_username = input()
    edited_password = input()
    
    # Array where credentials are added to.
    credentials = []

    try:
        # Opens the file then loops through it to find the credentials that need editing then appends it to an array.
        with open("Password Database.txt","r") as file:
            for x in file:
                decrypted_line = cipher.decrypt(x).decode()
                if service_to_edit in x:
                    decrypted_line = f'Service: {service_to_edit.capitalize()} Username: {edited_username}, Password: {edited_password}.'
                    credentials.append(decrypted_line)
                else:
                    credentials.append(decrypted_line)
    except Exception as e:
            print(f"An unexpected error occurred: {e}")

    try:
        # Writes the updated arrays to the file.
        with open("Password Database.txt","w") as file:
            for x in credentials:
                encrypted_line = cipher.encrypt(x.encode())
                file.write(encrypted_line.decode() + '\n')
    except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Removes user-added credentials
def remove_credentials(cipher = Fernet(load_key())):
    
    # Asks the user for which service and it's credentials to remove.
    service_to_remove = input()
    
    # Array where credentials are added to.
    credentials = []
    
    try:
        # Opens the text file with credentials, it then loops through the list
        with open("Password Database.txt","r") as file:
            for x in file:
                decrypted_line = cipher.decrypt(x).decode()

                # Adds credentials that aren't the ones to remove
                if service_to_remove.capitalize() not in decrypted_line:
                    credentials.append(decrypted_line)

        # Writes the remaining credentials to the credentials file
        with open("Password Database.txt","w") as file:
            for x in credentials:
                encrypted_line = cipher.encrypt(x.encode())
                file.write(encrypted_line.decode() + '\n')
    except Exception as e:
            print(f"An unexpected error occurred: {e}")

# The managers menu
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
            print("Invaild Input")
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
    if True:
        while True:
            menu()

if __name__ == "__main__":
    main()