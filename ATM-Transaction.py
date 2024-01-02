import mysql.connector
from time import sleep

def database_connection():
    return mysql.connector.connect(
        host='127.0.0.1',
        database='banking_system',
        user='root',
        password='root123'
    )

def create_account():
    print("\nOpen a new bank Account:")
    choice = input("Do you want to open a new account? (Yes/No)").lower()

    if choice == 'yes':
        name = input("Enter you full name : ")
        dob = input("Enter your date of birth (YYYY-MM-DD): ")
        deposit_amount = float(input("Enter the amount you want to deposit : "))

        conn = database_connection()
        cursor = conn.cursor()

        try:

            cursor.execute("insert into accounts (name, dob, balance) values (%s, %s, %s)", (name, dob, deposit_amount))
            conn.commit()

            print("\nAccount created successfully!")
            print(f"Name: {name}, Date of Birth: {dob}")
            print(f"Your  account number: {cursor.lastrowid}")
            print(f"Total balance: {deposit_amount}")
        finally:
            cursor.close()
            conn.close()

        countdown(9)

    elif choice == 'no':
        print("Returning to the main menu.")
        countdown(9)

    else:
        print("Invalid choice. Returning to the main menu.")
        countdown(9)

def withdraw_money():
    print("\nWithdraw Money:")
    choice = input("Do you want to withdraw money? (Yes/No)").lower()

    if choice == 'yes':
        account_number = input("Enter your bank account number : ")
        withdraw_amount = float(input("Enter the amount you want to withdraw : "))

        conn = database_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (account_number,))
            current_balance = cursor.fetchone()[0]

            if current_balance >= withdraw_amount > 0:
                new_balance = current_balance - withdraw_amount
                cursor.execute("update accounts set balance = %s where account_number = %s", (new_balance, account_number))

                conn.commit()

                print("\nYou have sucessfully Withdraw the amount")
                print(f"Your Current Balance is - {new_balance}")
            else:
                print("\nInvalid withdrawal amount or insufficient balance.")

        finally:
            cursor.close()
            conn.close()

        countdown(9)

    elif choice == 'no':
        print("Returning to the main menu.")
        countdown(9)

    else:
        print("Invalid choice. Returning to the main menu.")
        countdown(9)

def deposit_money():
    print("\nDeposit Money:")
    choice = input("Do you want to Deposit money? (Yes/No)").lower()

    if choice == 'yes':
        account_number = input("Enter your bank account number : ")
        deposit_amount = float(input("Enter the amount you want to deposit : "))

        conn = database_connection()
        cursor = conn.cursor()

        try:

            cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (account_number,))
            current_balance = cursor.fetchone()[0]


            new_balance = current_balance + float(deposit_amount)
            cursor.execute("update accounts set balance = %s where account_number = %s", (new_balance, account_number))

            conn.commit()

            print("\nYou have sucessfully Deposit the amount")
            print(f"Your Current Balance is - {new_balance}")

        finally:
            cursor.close()
            conn.close()

        countdown(9)

    elif choice == 'no':
        print("Returning to the main menu.")
        countdown(9)

    else:
        print("Invalid choice. Returning to the main menu.")
        countdown(9)

def check_balance():
    print("\nCheck Balance:")
    choice = input("Do you want to see your balance? (Yes/No): ").lower()

    if choice == 'yes':
        account_number = input("Enter your account number: ")

        conn = database_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (account_number,))
            current_balance = cursor.fetchone()[0]
            print(f"\nYour current balance is: {current_balance}")

        finally:
            cursor.close()
            conn.close()

        countdown(9)

    elif choice == 'no':
        print("Returning to the main menu.")
        countdown(9)

    else:
        print("Invalid choice. Returning to the main menu.")
        countdown(9)


def countdown(seconds):
    for i in range(seconds, 0, -1): # (start, stop, stape)
        print(f"Returning to the main menu in {i} seconds...", end='\r')
        sleep(1)
    print("\n")

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Create bank account")
        print("2. Withdraw money")
        print("3. Deposit money")
        print("4. See balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_account()
        elif choice == '2':
            withdraw_money()
        elif choice == '3':
            deposit_money()
        elif choice == '4':
            check_balance()
        elif choice == '5':
            print("Thank you for using abc bank atm.see you again.Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main_menu()
