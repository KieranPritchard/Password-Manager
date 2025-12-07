from cryptography.fernet import Fernet
import hashlib
import sys
import os

# class for password manager
class password_manager():
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