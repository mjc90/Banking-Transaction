# Banking-Transaction Project

This repository contains a project completed during my Python training. This project was completed using a combination of Python and My-SQL database.


## Authors

- [@mjc90](https://github.com/mjc90/Banking-Transaction.git)


## Project Details

| Project Name                           | Description                                                                                             | Tools & Technologies Used     |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------- | -------------- |
| Banking-Transaction                 | The Python-based Banking System uses MySQL for account management and transactions through a command-line interface.                                 |  Python, MySQL, MySQL Connector for Python  |


## Getting Started


# Project - Banking-Transaction

The Banking System Application is a Python-based program that facilitates various banking operations such as creating a new account, withdrawing money, depositing money, and checking account balance. The application interacts with a MySQL database to store and retrieve account details, ensuring secure and reliable banking operations.


## Key Features:


#### 1. Database Connection:

* Utilizes the mysql.connector library to establish a connection with a MySQL database named banking_system.
* The database credentials include the host, database name, user, and password, ensuring secure access to the banking system.

#### 2. Account Operations:

* Create Account: Allows users to open a new bank account by providing their full name, date of birth, and initial deposit amount. The application inserts the account details into the accounts table, generating a unique account number for identification.
* Withdraw Money: Enables account holders to withdraw money from their accounts by specifying the account number and withdrawal amount. The application verifies the account balance and updates the balance after a successful withdrawal.
* Deposit Money: Facilitates account deposits by allowing users to specify the account number and deposit amount. The application updates the account balance after a successful deposit transaction.
* Check Balance: Provides account holders with the ability to check their account balance by entering their account number. The application retrieves and displays the current account balance from the database.

#### 3. Database Schema:

* Defines a database schema named banking_system with a single table named accounts.
* The accounts table structure includes columns for account_number (Primary Key), name, dob (Date of Birth), and balance.
* Stores account details such as account number, account holder's name, date of birth, and account balance in the accounts table, facilitating efficient account management and retrieval.

#### 4. User Interface:

* Presents users with a main menu interface, offering options to create a bank account, withdraw money, deposit money, check balance, or exit the application.
* Validates user input and navigates users through various banking operations, ensuring a user-friendly and interactive experience.

## Implementation:

#### * Programming Language: Python
#### * Database: MySQL
#### * Database Connector: mysql.connector
#### * Database Schema: banking_system with accounts table
#### * User Interface: Command-Line Interface (CLI)
#### * Operations: Account Creation, Withdrawal, Deposit, Balance Checking

##  Conclusion: 
The Banking System Application provides a comprehensive solution for managing banking operations through a user-friendly interface. By integrating with a MySQL database, the application ensures secure and efficient account management, enabling users to perform essential banking tasks conveniently.

## Contributing

Contributions are always welcome!

If you have any feedback or suggestions for improvements, please feel free to open an issue or pull request.

