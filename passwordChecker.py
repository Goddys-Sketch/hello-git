import string
import getpass


password = input("Enter password for checking: ")
#password = password + " "

reEnterPassword = input("Enter password again: ")


def checkPassword(password):

    #error = 0

    if password == "" or " ":
        print("Password is empty")
        exit()

    if any(char.islower() for char in password) == False:
        print("Password must contain atleast one lowercase letter")
        exit()


    #Checks if there is a lowercase character to prevent all capital characters like AAAAA
    if any(char.isupper() for char in password) == False:
        print("Password must contain atleast one lowercase letter")
        exit()

    #Checks if there is an uppercase character to prevent all lower case characters like aaaaaa
    if any(char in string.punctuation for char in password) == False:
        print("Password must contain atleast one special character")
        exit()


    #Checks if there is a symbol in the password
    if len(password) <= 5:
        print("Password is too short")
        exit()

    #Checks if the password is less than 9 characters
    if len(password) >= 20 == False:
        print("Password is too long")
        exit()

    #Checks if the password is too long
    if any(char.isdigit() for char in password) == False:
        print("Password must contain atleast one number")
        exit()

    #Checks if the password contains a digit


    count =0

    passwordSpace = password + " "

    for i in range(len(passwordSpace)-1):
        if passwordSpace[i] == passwordSpace[i+1]:
            count = count + 1
        #if (i+1) == len(password):
         #   break;


    if count >= 3:
        print(count)
        print("Password must not contain more than 2 repeating letters")
        exit()

    #return True

    if password != reEnterPassword:
        print("Password does not match")
        exit()

    return True

setPassword = ""

if checkPassword(password) == True:
    setPassword = setPassword + password

print("This is your password " + setPassword + " and it is accepted! ")

#The program is now completed however, one major and big upgrade would be to asterisk or hide the input when entering the password for checking
