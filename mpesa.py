print(" Welcome To Mpesa Menu ")
print("                   ")
print("1. Send Money")
print("2. Withdraw Cash")
print("3. Buy Airtime")
print("4. Pay Bill")
print("0. Exit")
print("           ")

choice = input("Enter your choice (0-4): ").strip()

if choice == '1':
        print(" SEND MONEY ")
        recipient = input("Enter recipient phone number: ")
        amount = input("Enter amount: ")
        print(f"Request sent: Sending KES {amount} to {recipient}.")

elif choice == '2':
        print(" WITHDRAW CASH ")
        agent_no = input("Enter Agent Number: ")
        amount = input("Enter amount to withdraw: ")
        print(f"Request sent: Withdrawing KES {amount} from agent {agent_no}.")

elif choice == '3':
        print(" BUY AIRTIME ")
        #i have to create a nested if --else to handle the inner menu
        airtime_option = input("1. For my number\n2. For other number\nEnter choice (1 or 2): ")
        
        if airtime_option == '1':
            amount = input("Enter amount: ")
            print(f"Request sent: Buying KES {amount} Airtime for your number.")
        elif airtime_option == '2':
            number = input("Enter other number: ")
            amount = input("Enter amount: ")
            print(f"Request sent: Buying KES {amount} Airtime for {number}.")
        else:
            print("       ")
            print("Invalid Airtime choice. Returning to main menu.")

elif choice == '4':
        print("\n PAY BILL")
        business_no = input("Enter Business Number: ")
        account_no = input("Enter Account Number : ")
        amount = input("Enter amount: ")
        print(f"\n Request sent: Paying KES {amount} to Business {business_no}.")

elif choice == '0':
        print("\n Exiting M-Pesa Menu. Thank you!")
        
else:
    print("              ")
    print(f" Invalid choice '{choice}'. Please select a number from 0 to 4.")