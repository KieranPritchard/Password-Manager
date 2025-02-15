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

### Objective:
To create another cyber security based project, around password security. I also wanted to pursue a project that uses CRUD (Create, Read, Update, Delete), to build skills with persistent storage.
### Technology and Tools Used:
* **Language:** Python.
* **Framework/Library:** Cryptography.
* **Tools:** VS Code.
### Challenges Faced:
Firstly, there was a problem when converting the user input into hashes. this was fixed by changing `.update()` to the librarys `.digest()` function. Then finally I had a problem with the `edit_credentials()` and `delete_credentials()` luckily however, I had managed to come to the solution that is used in the program.
### Outcome:
Successfully created another cyber security project, using cyber security based external libraries and password security knowledge. Also managed to implement CRUD methodologies into a project.
## How to Use the Project
1. **Clone The Repository:**
	* Download the project to your local device, this can be done with git.
2. **Set-up The Key:**
	* run the script to generate an encryption key, named `key.key`. 
	* This automatically saves the file to the specified path.
	* Please ensure the key is stored securely, as not only does it allow encryption to take place. its essential to making the program work.
3. **Login:**
	  * When you are prompted, enter the username and password. 
	  * The default values are hashed values in the code, you may modify these hashes if desired.
4. **Using The Password Manager:**
	* After you have successfully logged in. You may access the following features:
		* **Adding a new credentials:** This allows you to input and save new credentials for various accounts.
		* **Viewing saved credentialls:** This decrypts and views stored passwords.
5. **Running The Code**
	* Navigate to the directory storing the project. Then use this command: `python Password_Manager.py`.
	* Follow the onscreen prompts for login and accesssing features.
## Licenses
License is located in the root of the repository.