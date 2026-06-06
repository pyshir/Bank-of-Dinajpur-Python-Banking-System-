# Bank of Dinajpur (Python Banking System)

A simple command-line banking system written in Python. This project demonstrates the use of:

* File Handling (CSV files)
* Dictionaries
* Functions
* Decorators
* User Authentication
* Transaction History
* Date & Time Management

## Features

### 1. Create Account

* Create a new bank account.
* Generates a random 4-digit PIN.
* Stores user data in `balance.csv`.

### 2. Deposit Money

* Login using phone number and PIN.
* Deposit money into an account.
* Updates account balance.

### 3. Withdraw Money

* Login using phone number and PIN.
* Withdraw money from an account.
* Updates account balance.

### 4. Balance Check

* Login using phone number and PIN.
* View current account balance.

### 5. PIN Change

* Login using current PIN.
* Change account PIN.

### 6. Transaction History

* Generates a transaction history file.
* Stores all account activities.

---

## Project Structure

```
Bank_of_Dinajpur/
│
├── main.py
├── balance.csv
├── history.txt
├── user_name.csv
└── README.md
```

### balance.csv

Stores account information.

Example:

```csv
Name,Phone,Pin,Balance
Jahid,017XXXXXXXX,1234,5000
```

### User Transaction File

Each user gets a separate CSV file.

Example: `Jahid.csv`

```csv
06/06/2026 12:23:15 PM,Deposit,100
06/06/2026 12:30:10 PM,Withdraw,50
```

---

## Requirements

Python 3.x

No external libraries are required.

Modules used:

```python
random
sys
datetime
time
```

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/bank-of-dinajpur.git
```

Move into the project directory:

```bash
cd bank-of-dinajpur
```

Run the program:

```bash
python main.py
```

---

## Menu

When the program starts, you will see:

```text
1.Create Account
2.Deposit
3.Withdraw
4.Balance Check
5.Pin Change
6.Transaction History
```

Choose an option by entering the corresponding number.

---

## Example Workflow

### Create Account

```text
Enter Your name:
= Jahid

Enter Your phone:
= 017XXXXXXXX

Enter initial deposit:
= 1000
```

Output:

```text
Your Pin is, 4321
Please save it, we don't have your pin code backup
```

### Deposit

```text
Enter Your phone:
= 017XXXXXXXX

Enter Your pin:
= 4321

How much do you want to deposit?
= 500
```

Output:

```text
Successfully Deposited 500 BDT
```

---

## Learning Objectives

This project is useful for beginners learning:

* Python Functions
* Dictionaries
* File Handling
* CSV Data Storage
* Decorators
* Authentication Systems
* Basic Banking Logic

---

## Known Limitations

* Data is stored in plain CSV files.
* PINs are not encrypted.
* No exception handling for invalid file operations.
* No balance validation before withdrawal.
* No account deletion feature.
* Usernames are used as transaction file names.

---

## Future Improvements

* Password/PIN encryption
* Account deletion
* Money transfer between users
* Input validation
* Better transaction reports
* Database integration (SQLite/MySQL)
* Object-Oriented Programming (OOP) version
* Graphical User Interface (GUI)

---

## License

This project is created for learning and educational purposes.
