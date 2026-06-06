import random
import sys
from datetime import datetime
import time


now = datetime.now()
time_now = now.strftime('%d/%m/%Y %I:%M:%S %p')

balance_csv = {} #data will load here to update & re-write

def login_note(fx):
    def mfx(w,v):
        print('Welcome to Bank_of_Dinajpur\nTrying to login..')
        time.sleep(1)
        fx(w,v)
        print('Successfully login to Bank_of_Dinajpur!')
        time.sleep(1)
    return  mfx


def load_data():
    with open('balance.csv', 'r') as f:
        next(f)
        for i in f:
            name, phone, pin, balance = i.split(',')
            balance = (str(balance)).replace('\n', '')
            balance_csv[name]  = [phone,str(pin),balance]

def write_data():
    with open('balance.csv', 'w') as g:
        g.write('Name,Phone,Pin,Balance\n')
        for a,b in balance_csv.items():
            g.write(f'{a},')
            count = 0
            for c in b:
                g.write(f'{c}')
                if count <= 1:
                    g.write(f',')
                count += 1

            g.write('\n')

def update_data_deposit(a,b,c):
    for i,j in balance_csv.items():
        if j[0] == a and j[1] == b:
            j[2] = str(int(j[2]) + int(c))
            break

def update_data_withdraw(a,b,c):
    for i,j in balance_csv.items():
        if j[0] == a and j[1] == b:
            j[2] = str(int(j[2]) - int(c))
            break

def balance_check(a,b):
    for i,j in balance_csv.items():
        if j[0] == a and j[1] == b:
            print(f'Current balance is, {j[2]} BDT')
            break

def pin_change(a,b,c):
    for i,j in balance_csv.items():
        if j[0] == a and j[1] == b:
            j[1] = c
            break

def save_history(user, date, op, update):
    with open(f'{user}.csv', 'a') as t:
        t.write(f'{date},{op},{update}\n')

@login_note
def pin_check(w,v): #login method
    for x,y in balance_csv.items():
        if y[0] == w and y[1] == v:
            break
        else:
            sys.exit('Login detail don\'t match, Error!')

def user_check(w): #duplicate account finder
    for x,y in balance_csv.items():
        if y[0] == w:
            sys.exit('User already exist')

def load_history(a):
    with open(f'{a}.csv', 'r') as f:
        for i in f:
            i = i.strip().split(',')
            balance_csv[i[0]] = i[1:]

def write_history():
    with open('t_history.txt', 'w') as f:
        f.write(f'All transaction history\n\n\n')
        for i, j in balance_csv.items():
            f.write(f'{i}    ')
            count = 0
            for k in j:
                f.write(f'{k}')
                if count < len(j) - 1:
                    f.write(' ')
                else:
                    f.write(f'\n')
                count += 1




if __name__ == '__main__': #program starts from here
    operation = input('1.Create Account\n2.Deposit\n3.Withdraw\n4.Balance Check\n5.Pin Change\n6.Transaction History\n')

    if operation == '1': #Create Account
        load_data()
        client_name = input('Enter Your name:\n=')
        client_phone = input('Enter Your phone:\n=')
        user_check(client_phone)
        client_pin = random.randint(1000, 9999)
        initial_deposit = input('Enter initial deposit:\n=')
        balance_csv[client_name] = [client_phone,client_pin,initial_deposit]
        write_data()
        print(f'Your Pin is, {client_pin}\nPlease save it, we don\'t have your pin code backup')
        save_history(client_name,time_now,'Create Account','Successful')

    elif operation == '2': #Deposit
        load_data()
        client_name = input('Enter your Account\'s Name\n=')
        client_phone = input('Enter Your phone:\n=')
        client_pin = input('Enter Your pin:\n=')
        pin_check(client_phone, client_pin)
        deposit_amount = input('How much do you want to deposit?\n=')
        update_data_deposit(client_phone,client_pin,deposit_amount)
        write_data()
        print(f'Successfully Deposited {deposit_amount} BDT')
        save_history(client_name,time_now,'Deposit', deposit_amount)

    elif operation == '3': #Withdraw
        load_data()
        client_name = input('Enter your Account\'s Name\n=')
        client_phone = input('Enter Your phone:\n=')
        client_pin = input('Enter Your pin:\n=')
        pin_check(client_phone, client_pin)
        withdraw_amount = input('How much do you want to withdraw?\n=')
        update_data_withdraw(client_phone,client_pin,withdraw_amount)
        write_data()
        print(f'Successfully Withdraw {withdraw_amount} BDT')
        save_history(client_name,time_now,'Withdraw', withdraw_amount)

    elif operation == '4': #Check Balance
        load_data()
        client_name = input('Enter your Account\'s Name\n=')
        client_phone = input('Enter Your phone:\n=')
        client_pin = input('Enter Your pin:\n=')
        pin_check(client_phone, client_pin)
        balance_check(client_phone,client_pin)
        save_history(client_name,time_now,'Balance Check','' )

    elif operation == '5': #Pin Change
        load_data()
        client_name = input('Enter your Account\'s Name\n=')
        client_phone = input('Enter Your phone:\n=')
        client_pin = input('Enter Your CURRENT pin:\n=')
        pin_check(client_phone, client_pin)
        new_pin = input('Enter your NEW pin\n=')
        confirm_new_pin = input('Enter your NEW pin Again to Confirm\n=')
        pin_change(client_phone,client_pin,new_pin)
        print('Pin Changed Successfully!')
        write_data()
        save_history(client_name,time_now,'Pin Change',new_pin)

    elif operation == '6': #history generate
        client_name = input('Enter your name\n=')
        load_history(client_name)
        write_history()
        print(f'{client_name}\'s all transaction history has been generated as history.txt Successfully!')
        save_history(client_name,time_now,'Generate history', 'Successful')

