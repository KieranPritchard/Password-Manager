# Password Manager

<div align="center">
    <img alt="GitHub Created At" src="https://img.shields.io/github/created-at/KieranPritchard/Password-Manager">
    <img alt="GitHub License" src="https://img.shields.io/github/license/KieranPritchard/Password-Manager">
    <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/t/KieranPritchard/Password-Manager">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/KieranPritchard/Password-Manager">
    <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/KieranPritchard/Password-Manager">
    <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/KieranPritchard/Password-Manager">
</div>

## Project Description

This project is a password manager, it allows users to save their usernames and password to an encrypted file for safe keeping and easy access. 

The reason i built this project, was because wanted another cyber security project to do. I also wanted to a project with some form of the CRUD framework (Create, Read, Update, and Delete), the four systems to create storage manipulation in a system or app.

I had some problems with the program, but thankfully with time and research i managed to remove them. Firstly, there was a problem involving the hashs of the inputs in the login function. this was fixed by removing the `.update()` function from the code of the function and replacing it with replacing it with `.digest` function, this was what i should of had orignally instead of `.update()`. finally, i had a problem with creating the `edit_credentials()` and `delete_credentials()` functions. the problem with these was i was'nt sure on how to implement them, i slowly worked out a way how to which is the version you do.

## How to Use the Project

1. **Clone The Repository:**

   Download the project to your local device, this can be done with git.

2. **Set-up The Key:**

   Firstly, run the script to generate an encryption key, named key.key. this automatically saves the file to the specified path.
    Finally, please ensure the key is stored securely, as not only does it allow encryption to take place. its essiental to making the program work.

3. **Login:**

    When you are prompted, enter the username and password. the default values are hashed values in the code, you may modify these hashes if desired.

4. **Using The Password Manager:**
    
    After you have successfully logged in. You may access the following features:
   * **Adding a new credentials:** This allows you to input and save new credentials for various accounts.
   * **Viewing saved credentialls:** This decrypts and views stored passwords.

5. **Running The Code**

* Navigate to the directory storing the project. Then use this command: `python Password_Manager.py`.
* Follow the onscreen prompts for login and accesssing features.


## Licenses

License is located in the "doc" folder.
