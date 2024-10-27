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

## How to Install and Run the Project

## How to Use the Project

## Licenses

License is located in the "doc" folder.
