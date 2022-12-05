# This is a username and password program created in python with database internally
import getpass
database = {"vipulraj01": "123456", "vipulraj02": "000000"}
username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again : ")
        break
print("Verified")
