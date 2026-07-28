import random
import json
import string
try:
    with open("passwords.json","r") as pm:
        accounts=json.load(pm)
except FileNotFoundError:
    accounts=[]


def rem_password():
    pass_len=12
    password=""
    all_values=string.ascii_letters + string.digits + string.punctuation
    for i in range(pass_len):
        password += random.choice(all_values)
    return password


def read_the_json():
    global accounts
    with open("passwords.json","r") as pm:
       accounts=json.load(pm)

        
def write_in_json():
    global accounts
    with open("passwords.json","w") as pm:
        json.dump(accounts,pm,indent=4)

        
def few_passwd():
        condition=input("CREATE A PASSWORD BY OWN OR CHOICE RANMDOM PASSWORD (YES/NO) : ")
        
        if condition.upper()=="YES":
            passwd = input("Enter password: ")
            while len(passwd) < 8:
                print("Password must be at least 8 characters.")
                passwd = input("Enter password: ")
            return passwd
        else:
            x=rem_password()
            print(x," this random password will be saved")
            return x

        
def add_accounts():
    website=input("Enter your website : ")
    username=input("Enter your username : ")
    Password=few_passwd()
    account={
        "Website" : website,
        "Username" : username,
        "Password" : Password
        }
    accounts.append(account)
    print("Congratulations!! Your account successfully created")
    write_in_json()

    
def view_all_accounts():
    read_the_json()
    if not accounts:
        print("Sorry!! There is no any account.")
        return
    for i in  accounts:
        print(i)

        
def search_accounts():
    read_the_json()
    if not accounts:
        print("Sorry!! There is no any account.")
        return
    found=False
    website=input("Enter the account website to search : ")
    for i in accounts:
        if i["Website"] == website:
            found=True
            print("Found!")
            print("Username :",i["Username"])
            print("Password : ",i["Password"])
            print()
    if found==False:
        print("Sorry!! Your Website is incorrect please try again to search.")

        
def update_accounts():
    read_the_json()
    if not accounts:
        print("Sorry!! There is no any account.")
        return
    found=False
    website=input("Enter the account website to update your password : ")
    for i in accounts:
        if i["Website"]==website:
            found=True
            i["Password"]=few_passwd()
            print("Congratulation your password updated successfully.")
            write_in_json()
            break
    if found==False:
        print("Sorry!! Your website not be found so we can't upadte the password")

        
def delete_accounts():
    read_the_json()
    if not accounts:
        print("Sorry!! There is no any account.")
        return
    found=False
    website=input("Enter your account website to delete your account permanently if don't know press(NO) : ")
    username=input("Enter your account username to delete your account permanently : ")
    for i in accounts:
        if i["Website"] == website and i["Username"] == username:
            found=True
            accounts.remove(i)
            print("Congrates!! Your account deleted successfully")
            write_in_json()
            break
    if found==False:
        print("Sorry!! Your username and website are incorrect so we can't be deleted")

        
while True:
    print("\n===== Password Manager =====")
    print("1. Add Accounts")
    print("2. View All Accounts")
    print("3. Search Accounts")
    print("4. Update Password")
    print("5. Delete Account")
    print("6. Exit")
    choice=input("Enter your choice : ")
    match choice:
        case "1":
            add_accounts()
        case "2":
            view_all_accounts()            
        case "3":
            search_accounts()
        case "4":
            update_accounts()
        case "5":
            delete_accounts()
        case "6":
            print("Exit form accounts goodbayee")
            break
        case _:
            print("Invalid choice Try Aagin!!")
    

    
    
        
    
