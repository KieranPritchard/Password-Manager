from cryptography.fernet import Fernet
import os
import sys

# class for password manager
class passwordManager():
    def __init__(self, key, database):
        self.__key = key
        self.__database = database

    # Function to add password
    def addPassword(self):
        # Creates a cipher object with the key
        with open(self.__key, "rb") as f:
            key = f.read()
        cipher = Fernet(key)
        
        # Asks the user to input their username, password, and services
        username = input("Please input username: ")
        password = input("Please input password: ")
        service = input("Please input service: ")

        # Formats the users credentials as a string 
        credentials = f"Service: {service}, Username: {username}, Password: {password}"

        # Encrypts the credentials using fernet
        encrypted_creds = cipher.encrypt(credentials.encode())

        # Trys opening a file
        try:
            # Opens the file listed in the database
            with open(self.__database, "a") as f:
                # Writes credentials to the file
                f.write(encrypted_creds.decode() + '\n')
        except Exception as e:
            # Outputs the error
            print(f"Error Encountered: {e}")

    # Function to read the passwords stored
    def readPassword(self):
        # Creates a cipher object with the key
        with open(self.__key, "rb") as f:
            key = f.read()
        cipher = Fernet(key)

        # stores the credentials in a list
        credentials = []

        # Trys to open the database and get the credentials
        try:
            # Opens the database file
            with open(self.__database) as f:
                # loops through the file
                for line in f:
                    # Decrypts the line from the file
                    decrypted = cipher.decrypt(line.strip().encode()).decode()
                    # Adds the line to the list
                    credentials.append(decrypted)
        except Exception as e:
            # Outputs the error
            print(f"Error: {e}")

        # loops through the list
        for cred in credentials:
            # Outputs the credentials
            print(cred)
    
    def editCredentials(self):
        # Creates a cipher object with the key
        with open(self.__key, "rb") as f:
            key = f.read()
        cipher = Fernet(key)

        # Asks the user to input their credentials
        service = input("Please input the service you want to edit: ")
        username = input("Please input the new username: ")
        password = input("Please input the new password: ")

        # Stores credentials
        edited_creds = []

        # Tries to open the password file and add the credentials
        try:
            # Opens the file to read it
            with open(self.__database, "r") as f:
                # loops over the file
                for cred in f:
                    # Decrypts the lines
                    decrypted_cred = cipher.decrypt(cred.strip().encode()).decode()
                    #Check if the credentials match the edited ones
                    if decrypted_cred.lower().startswith(f"service: {service.lower()}"):
                        # adds the edit to the decrypted line
                        decrypted_cred = f"Service: {service}, Username: {username}, Password: {password}"
                    # Adds the decrypted credential to a list
                    edited_creds.append(decrypted_cred)

            # Opens the file to write the edit to it
            with open(self.__database, "w") as f:
                # Loops over it again and adds back in the files
                for cred in edited_creds:
                    # Encrypts the credential
                    encrypted_cred = cipher.encrypt(cred.encode())
                    # Adds it back to file
                    f.write(encrypted_cred.decode() + '\n')

        # Outputs error message
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def removeCredentials(self):
        # Creates a cipher object with the key
        with open(self.__key, "rb") as f:
            key = f.read()
        cipher = Fernet(key)

        # Asks the user for which service and its credentials to remove.
        service_to_remove = input("Please input the service you want to remove: ")
        # Array where credentials are added to.
        credentials = []
        
        # Try's to open the file and remove the credentials
        try:
            # Opens the text file with credentials, it then loops through the list
            with open(self.__database, "r") as f:
                # Loops through the credentials in the file
                for cred in f:
                    # decrypts the current line 
                    decrypted_line = cipher.decrypt(cred.strip().encode()).decode()
                    # Adds credentials that aren't the ones to remove
                    if not decrypted_line.lower().startswith(f"service: {service_to_remove.lower()}"):
                        # Adds the credentails to the list
                        credentials.append(decrypted_line)

            # Writes the remaining credentials to the credentials file
            with open(self.__database, "w") as f:
                # Loops through the credentials in the list
                for cred in credentials:
                    # Encrypts the current line
                    encrypted_line = cipher.encrypt(cred.encode())
                    # Writes it to the file
                    f.write(encrypted_line.decode() + '\n')

        # Catches errors and outputs it
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Standalone function for the main, with object passed in
def menu(object):
    print("(1) - Add Credentials\n(2) - Read Credentials\n(3) - Edit Credentials\n(4) - Remove Credentials\n(5) - Exit")
    print("=" * 30)

    try:
        # Asks the user for what option they want
        user_selection = int(input("Please Select Option: "))

        # Checks what function to use based on users selection
        if user_selection == 1:
            # Calls the add credentials method
            object.addPassword()
        elif user_selection == 2:
            # Calls the read credentials method
            object.readPassword()
        elif user_selection == 3:
            # Calls the edit credentials method
            object.editCredentials()
        elif user_selection == 4:
            # calls the remove credentials method
            object.removeCredentials()
        elif user_selection == 5:
            sys.exit()
        else:
            print("Invalid Input")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Gets base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Gets the key and the database
    key = os.path.join(BASE_DIR, "res/key.key")
    database = os.path.join(BASE_DIR, "res/Password Database.txt")

    # Creates manager object
    manager = passwordManager(key,database)

    # Header for the program
    print("=" * 30)
    print("Password Manager")
    print("=" * 30)
    
    # Runs the menu indefinately intill it is broken
    while True:
        # Calls the menu each time
        menu(manager)

# Starts the progam
if __name__ =="__main__":
    main()