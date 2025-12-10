from cryptography.fernet import Fernet
import os

# class for password manager
class passwordManager():
    def __init__(self, key, database):
        self.key = key
        self.database = database

    # Function to add password
    def add_password(self):
        # Creates a cipher object
        cipher = Fernet(self.key)
        
        # Asks the user to input their username, password, and services
        username = input("Please input username: ")
        password = input("Please input password: ")
        service = input("Please input service: ")

        # Formats the users credentials as a string 
        credentials = f"Service: {service}, Username, {username}, Password: {password}"

        # Encrypts the credentials using fernet
        encrypted_creds = cipher.encrypt(credentials.encode())

        # Trys opening a file
        try:
            # Opens the file listed in the database
            with open(self.database) as f:
                # Writes credentials to the file
                f.write(encrypted_creds.decode() + '\n')
        except Exception as e:
            # Outputs the error
            print(f"Error {e}")

    # Function to read the passwords stored
    def read_password(self):
        # Creates a cipher object
        cipher = Fernet(self.key)

        # stores the credentials in a list
        credentials = []

        # Trys to open the database and get the credentials
        try:
            # Opens the database file
            with open(self.database) as f:
                # loops through the file
                for line in f:
                    # Decrypts the line from the file
                    decrypted = cipher.decrypt(line).decode()
                    # Adds the line to the list
                    credentials.append(decrypted)
        except Exception as e:
            # Outputs the error
            print(f"Error: {e}")
        # loops through the list
        for cred in credentials:
            # Outputs the credentials
            print(cred)
    
    def edit_credentials(self):
        # Creates a cipher object
        cipher = Fernet(self.key)

        # Asks the user to input their credentials
        service = input("Please input the service you want to edit: ")
        username = input("Please input the new username: ")
        password = input("Please input the new password: ")

        # Stores credentials
        edited_creds = []

        # Tries to open the password file and add the credentials
        try:
            # Opens the file to read it
            with open(self.database, "r") as f:
                # loops over the file
                for cred in f:
                    # Decrypts the lines
                    decrypted_cred = cipher.decrypt(cred).decode()
                    #Check if the credentials match the edited ones
                    if service in decrypted_cred:
                        # adds the edit to the decrypted line
                        decrypted_cred = f"Service: {service.capitalize()} Username: {username}, Password: {password}."
                    # Adds the decrypted credential to a list
                    edited_creds.append(decrypted_cred)
            # Opens the file to write the edit to it
            with open(self.database, "w") as f:
                # Loops over it again and adds back in the files
                for cred in edited_creds:
                    # Encrypts the credential
                    encrypted_cred = cipher.encrypt(cred.encode())
                    # Adds it back to file
                    f.write(encrypted_cred.decode() + '\n')
        # Outputs error message
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def remove_credentials(self):
        # Creates a cipher object
        cipher = Fernet(self.key)
        # Asks the user for which service and its credentials to remove.
        service_to_remove = input("Please input the service you want to remove: ")
        # Array where credentials are added to.
        credentials = []
        
        # Try's to open the file and remove the credentials
        try:
            # Opens the text file with credentials, it then loops through the list
            with open(self.database, "r") as f:
                # Loops through the credentials in the file
                for cred in f:
                    # decrypts the current line 
                    decrypted_line = cipher.decrypt(cred).decode()
                    # Adds credentials that aren't the ones to remove
                    if service_to_remove not in decrypted_line:
                        # Adds the credentails to the list
                        credentials.append(decrypted_line)
            # Writes the remaining credentials to the credentials file
            with open(self.database, "w") as f:
                # Loops through the credentials in the list
                for cred in credentials:
                    # Encrypts the current line
                    encrypted_line = cipher.encrypt(cred.encode())
                    # Writes it to the file
                    f.write(encrypted_line.decode() + '\n')
        # Catches errors and outputs it
        except Exception as e:
            print(f"An unexpected error occurred: {e}")