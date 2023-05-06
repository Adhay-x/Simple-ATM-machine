import time as t

userPin = 1234
userBalance = 97342.88
userName = "Adepoju Ayomide"
mylist = [1234, 1111, 5643]
print(f"Welcome to your Bank Account {userName} ")
print("\n")

while(True):
    print("\t1. Logout and exit")
    print("\t2. View account balance")
    print("\t3. Withdraw cash")
    print("\t4. Deposit cash")
    print("\t5. Change pin")
    print("\n")
    choice = int(input("Enter number to proceed:"))
    print("\n")

    if choice == 1:
        print("Exiting.....")
        t.sleep(2)
        print("You have been logged out")
        break
    elif choice in (2,3,4,5):
        num_of_tries = 3
        while(num_of_tries != 0):
            inputPin = int(input("Please enter your 4-digit pin>>> "))

            userPin = 1234
            if inputPin == userPin:
                print("Account Authorized \n")

                if choice == 2:
                    print("Loading account....")
                    t.sleep(1.5)
                    print(f"Your current balance is ${userBalance} \n")
                    break
                elif choice == 3:
                    print("Opening cash withdrawal......")
                    t.sleep(1.5)

                    while(True):
                        withdrawAmt = float(input("Enter the amount you wish to withdraw>>> "))
                        if withdrawAmt > userBalance:
                            print(f"You cannot withdraw ${withdrawAmt} due to Insuffficient funds")
                            print("Please enter a lower amount")
                        else:
                            print(f"Withdrawing {withdrawAmt}")
                            confirm = input("Confirm Y/N>>> ")
                            if confirm == "y":
                                userBalance -= withdrawAmt
                                print(f"Amount withdrawn {withdrawAmt}")
                                print(f"Your remaining balance is {userBalance} \n")
                                break

                            else:
                                print("Cancelling Transaction....")
                                t.sleep(2)
                                print("Transaction Cancelled \n\n")
                                break
                elif choice == 4:
                    print("Loading cash deposit......")
                    t.sleep(2)
                    depositAmt = float(input("Enter the amount you will like to deposit>>> "))
                    print(f" Depositing {depositAmt}")
                    confirm = input("Confirm Y/N>>> ")
                    if confirm == "y":
                        userBalance += depositAmt
                        print(f"Amount Deposited {depositAmt}")
                        print(f"Updated Amount {userBalance} \n")
                        break

                    else:
                        print("Cancelling Transaction....")
                        t.sleep(2)
                        print("Transaction cancelled")
                        break

                elif choice == 5:
                    print("Loading pin change....")
                    t.sleep(1.5)
                    newPin = int(input("Enter your new pin: "))
                    print(f"Changing pin to {newPin}")
                    if userPin in mylist:
                        userPin = mylist.append(0)
                        print("Pin changed successfully \n\n")
                        break
                    else:
                        print("Cancelling pin change.....")
                        t.sleep(2)
                        print("Process Cancelled")
                        break

            else:
                num_of_tries -= 1
                print(f"Pin incorrect! num_of_tries left {num_of_tries}")
    else:
        print("Exiting.....")
        t.sleep(2)
        print("Thank you, you have been logged out")
