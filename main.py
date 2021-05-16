##print("""=====================================
##==========================================""")
print("Welcome to New African Bank")
##print("""=====================================
##==========================================""")
Trials = 3
UserPin = 1234

while Trials != 0:
    Pin = int(input("Please Enter Your 4 digit Pin Number: "))
    if Pin != UserPin:
        Trials -= 1
        print("Wrong pin Number, You Have",Trials,"Trials Left")
    else:
        Userchoice = input("d: Deposit or w: Withdraw: ")
        if Userchoice == "d":
            UserDeposit = input("Enter the Amount You would like to Deposit: ")
            print(UserDeposit, "R Have seen Deposited Into Your Accouunt")
        if Userchoice == "w":
            UserWithdraw = input("Enter The Amount You Would Like to Withdraw: ")
            print(UserWithdraw, "R Have been Withdrawn From Your Account")
    UserExit = input("Would You Like to contiune? Y/N: ")
    if UserExit == "N":
        print("Thank You For Using New African Bank")
        break
    else:
        continue
