# my code on ATM
# below is a stored record of ATM users in a dictionary {last_ATM_digit :[name, pin, balance]}
users = {"8956": ["Emma", 2356, 200000], "8923": ["Efosa", 5623, 85000], "8900": ["Anne", 8451, 895000]}

print("welcome to heritage bank ATM")

# this set a loop for customer to keep trying as long details entered is not in the dictionary
while True:
    card = input("please enter the last digit of your card: ")
    if card not in users.keys():
        print("invalid last digit inputted")
        continue
    else:
        print(f"welcome {users[card][0]}")
        break


# this code entails the next step where the user input his/her pin
while True:
    while True:
        pin = int(input("input your four digit number: "))
        if pin == users[card][1]:
            print(""" please select your transaction:
            1 = View balance
            2 = Transfer
            3 = withdraw""")
            a = int(input())
            break
        else:
            print("incorrect pin")


# for balance check
    if a == 1:
        print(f"your account balance is: {users[card][2]}")
    

# for transfer
    elif a == 2:
        print("enter the amount you want to transfer")
        amount = int(input())

        while amount > users[card][2]:
            print(f"amount entered has exceeded account balance. \n Please enter amount less than {users[card][2]}")
            amount = int(input())
            continue

        print("Please enter the reciever account number")
        reciever_acct_no = input()
        while len(reciever_acct_no) > 10:
           print("invalid account number. \nplease input valid account number")
           reciever_acct_no = int(input())
           continue
    

        print(""" please select the reciever bank:
        1 = Heritage bank
        2 = GTbank
        3 = Zenith bank
        4 = UBA
        5 = Ecobank
        6 = Wema bank""")
    # input is supposed to be here but will ignore for the now because i dont have access to dictionaries of other bank
        print("please wait while your transaction is processing")
        print("initializing......")
        print("Transaction successful")
        print("Would you like to print your reciept. Y/N")
        s = input()
        if s == "Y":
            print("please take your reciept")
        else:
            print()

# for withdrawal
    elif a == 3:
        print("select the amount you want to withdraw")
        withdraw_val = int(input())
        while True:
            if withdraw_val > users[card][2]:
                print(f"the amount entered have exceeded the maximum withdrawal limit. \n please enter an amount less than {users[card][2]}")
                withdraw_val = int(input())
                continue
            else:
                print("please wait while your transaction is processing")
                print("initializing......")
                print("Transaction is succeful")
                break

        print("would you like a reciept for your transction Y/N: ")
        select = input().upper()
        if select == "Y":
            print("kindly take your reciept")


    end_tranx = input("would you like to perform another transaction: Y/N").upper()

    if end_tranx == "Y":
        continue
    if end_tranx == "N":
        print("Thank you for banking with us")
        break

        

    
    
    
        
            