
print("""
********************

New African Bank

********************
""")

#Code below is for the input
def intro():
    name = input('Enter your name? ')
    age = int(input('Please enter your age? '))

    if age<=18:
        print("Error 404 Restart!")
    else:
        print("You can enter the site! Welcome " +name+ "!")
    return name, age

def password():
    Trials = 3
    UserPin = 1234
    Userchoice=""
    UserDeposit=""

    while Trials != 0:
        Pin= int(input('ENTER 4 DIGIT CODE'))
        if Pin != UserPin:
            Trials -= 1
            print('Wrong pin, Please try again!',Trials,'Trials left')
        else:
            User = input('d: Deposit or w: withdraw')
            if UserDeposit == "d":
                print(UserDeposit, 'R Have been deposited!')
            if Userchoice == 'w':
                UserWithdraw = input('Enter the amount you wanna Withdraw: ')
                print(UserWithdraw,'R has been withdrawn')
        UserExit = input('Would You like to contiune? ')
        if UserExit == 'N':    
            print('Thank You For Using New African Bank!')
            break
        else:
            continue





intro()
password()