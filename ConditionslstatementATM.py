import time as t

print('                        GTBank ATM MACHINE                         ')
name = input('Enter your full name:')
print(f'Welcome {name}, to GTBank')
pin = 1578
Acct_Balance = 175090333
attempts = 3

while attempts != 0:
    user_pin = int(input('Enter your 4 digit pin number:'))
    if user_pin == pin:
        print(' Your pin has been validated, You can proceed')

    else:
        attempts -= 1
        print(f'Your pin is invalid,You have {attempts} attempts left')
        continue
    if attempts == 0:
        print('You have entered an incorrect pin too much, therefore, your account has been blocked'
              '\nKindly return after 24hours, Thank You ')
        quit()

    user_choice = input("B: Balance Inquiry "
                        "\nW: Withdrawals"
                        "\nT: Bank Transfers "
                        "\nD: Deposit"
                        "\n:")
    if user_choice == "B":
        t.sleep(1.5)
        print(f"Your total balance is ${Acct_Balance}")

    if user_choice == "W":
        Withdrawal_U = int(input('Enter the amount to be withdrawn:'))
        TAcct_Balance = Acct_Balance - Withdrawal_U
        print("Withdrawal is processing...")
        t.sleep(1.8)
        print(f" You have withdrawn ${Withdrawal_U} from your account")
        print(f" Your remaining balance is ${TAcct_Balance}, Thank you for using GTBank")

    if user_choice == "T":
        options = '''
            1. GTBank            2. Other Banks
            '''
        print(options)
        options2 = (input('Select either of the options by typing the NumberID:'))

        if options2 == 1:
            name = input('Enter the name:')
            int(input('Enter the account number:'))
            Transfer_U = int(input('Enter the amount to be transferred:'))
            TAcct_Balance = Acct_Balance - Transfer_U
            print('Transaction is processing....')
            t.sleep(1.5)
            print(f'${Transfer_U} has been transferred successfully to {name} from your account')
            print(f'You have ${TAcct_Balance} remaining in your account ')

        if options2 == 2:
            options3 = '''
                    Select the bank required for the money to be transferred
            1. UNION BANK                        2. FIDELITY BANK
            
            3. ZENITH BANK                       4. UBA BANK
            
            5. POLARIS BANK                      6. WEMA BANK
            '''
            print(options3)

    New_Option = int(input('Select the bank by typing the NumberID:'))

    if New_Option == 1:
        name = input('Enter the name:')
        int(input('Enter the account number:'))
        Transfer_U = int(input('Enter the amount to be transferred:'))
        TAcct_Balance = Acct_Balance - Transfer_U
        print('Transaction is processing....')
        t.sleep(1.5)
        print(f'${Transfer_U} has been transferred successfully to {name} from your account')
        print(f'You have ${TAcct_Balance} remaining in your account ')

    elif New_Option == 2:
        name = input('Enter the name:')
        int(input('Enter the account number:'))
        Transfer_U = int(input('Enter the amount to be transferred:'))
        TAcct_Balance = Acct_Balance - Transfer_U
        print('Transaction is processing....')
        t.sleep(1.5)
        print(f'${Transfer_U} has been transferred successfully to {name} from your account')
        print(f'You have ${TAcct_Balance} remaining in your account ')

    elif New_Option == 3:
        name = input('Enter the name:')
        int(input('Enter the account number:'))
        Transfer_U = int(input('Enter the amount to be transferred:'))
        TAcct_Balance = Acct_Balance - Transfer_U
        print('Transaction is processing....')
        t.sleep(1.5)
        print(f'${Transfer_U} has been transferred successfully to {name} from your account')
        print(f'You have ${TAcct_Balance} remaining in your account ')

    elif New_Option == 4:
        name = input('Enter the name:')
        int(input('Enter the account number:'))
        Transfer_U = int(input('Enter the amount to be transferred:'))
        TAcct_Balance = Acct_Balance - Transfer_U
        print('Transaction is processing....')
        t.sleep(1.5)
        print(f'${Transfer_U} has been transferred successfully to {name} from your account')
        print(f'You have ${TAcct_Balance} remaining in your account ')

    elif New_Option == 5:
        name = input('Enter the name:')
        int(input('Enter the account number:'))
        Transfer_U = int(input('Enter the amount to be transferred:'))
        TAcct_Balance = Acct_Balance - Transfer_U
        print('Transaction is processing....')
        t.sleep(1.5)
        print(f'${Transfer_U} has been transferred successfully to {name} from your account')
        print(f'You have ${TAcct_Balance} remaining in your account ')

    elif New_Option == 6:
        name = input('Enter the name:')
        int(input('Enter the account number:'))
        Transfer_U = int(input('Enter the amount to be transferred:'))
        TAcct_Balance = Acct_Balance - Transfer_U
        print('Transaction is processing....')
        t.sleep(1.5)
        print(f'${Transfer_U} has been transferred successfully to {name} from your account')
        print(f'You have ${TAcct_Balance} remaining in your account ')

    if user_choice == "D":
        Deposit_U = int(input('Enter the amount to be deposited:'))
        TAcct_Balance = Deposit_U + Acct_Balance
        print('Deposition is progressing...')
        t.sleep(1.8)
        print(f' You have deposited ${Deposit_U} to your account')
        print(f" Your total balance is {TAcct_Balance}, Thank you for using GTBank")

        user_exit = input('Would you like to exit? Y/N: ')
        if user_exit == "Y/y":
            print(' Thank you for using GTBank, do have a great day')
            break
        else:
            continue
