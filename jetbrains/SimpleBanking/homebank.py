import sqlite3
import random

class Card:
    IIN = '400000'
    acc_number_len = 9
    pin_len = 4
    db_conn = None

    def __init__(self, db_conn=None,card_info=None):
        if not db_conn:
            self.db_conn = sqlite3.connect('card.s3db')
        else:
            self.db_conn = db_conn

        if not card_info:
            self.account_number = self._generate_random_number(Card.acc_number_len)
            self.luhn = self._generate_luhn_number(Card.IIN + self.account_number)

            self.card_number = Card.IIN+self.account_number+ self.luhn
            self.pin = self._generate_random_number(Card.pin_len)

            self.create_account(self.card_number, self.pin)
        else:
            self.card_number = card_info[0]
            self.account_number = card_info[0][:-1]
            self.luhn = card_info[0][-1]
            self.pin = card_info[1]

    def _generate_random_number(self, nr_len):
        nr=''
        for _ in range(nr_len):
            nr+=str(random.randint(0,9))
        return nr

    def _generate_luhn_number(self, bank_account_number):
        bin_digits = [int(digit) for digit in bank_account_number]
        luhn = 0
        for i in range(len(bin_digits)):
            if i%2==0:
                bin_digits[i]*=2
            if bin_digits[i]>9:
                bin_digits[i]-=9

        control_nr = sum(bin_digits)
        control_remainder = control_nr%10
        if control_remainder:
            luhn = 10 - control_remainder
        return str(luhn)

    def create_account(self, cn, pin):
        db_cur = self.db_conn.cursor()
        db_cur.execute(f'insert into card(number,pin) values ("{cn}","{pin}");')
        self.db_conn.commit()

    def add_income(self ,amount, card_number=None):
        if not card_number:
            card_number = self.card_number
        current_balance = self.get_balance(card_number)
        db_cur = self.db_conn.cursor()
        db_cur.execute(f'update card set balance = {current_balance+amount} where number="{card_number}";')
        self.db_conn.commit()

    def get_balance(self,card_number=None):
        if not card_number:
            card_number = self.card_number
        db_cur = self.db_conn.cursor()
        db_cur.execute(f'select balance from card where number = "{card_number}";')
        db_result = db_cur.fetchone()
        self.db_conn.commit()
        if db_result:
            return db_result[0]    
        return None

    def transfer(self, other_account):
        if self.card_number == other_account:
            return "You can't transfer money to the same account!\n"
        if self._generate_luhn_number(other_account[:-1])!=other_account[-1]:
            return "Probably you made a mistake in the card number. Please try again!\n"

        other_balance = self.get_balance(other_account)
        if other_balance == None:
            return "Such a card does not exist.\n"

        current_balance = self.get_balance()
        amount = int(input('Enter how much money you want to transfer:\n>'))
        if current_balance < amount:
            return "Not enough money!\n"
             
        self.add_income(-amount)
        self.add_income(amount,other_account)
        return 'Success!\n'
    
    def delete_account(self):
        db_cur = self.db_conn.cursor()
        db_cur.execute(f'delete from card where number="{self.card_number}";')
        self.db_conn.commit()
        return "The account has been closed!\n"


def main_screen(db_conn):
    while True:
        print(
'''1. Create an account
2. Log into account
0. Exit''')
        user_choice = input('>')
        if user_choice == '0':
            print('\nBye!')
            break
        elif user_choice == '1':
            user_card = Card(db_conn)
            print(
'''\nYour card has been created
Your card number:\n{}\nYour card PIN:\n{}\n'''.format(user_card.card_number, user_card.pin))
        elif user_choice == '2':
            card_info = user_login(db_conn)
            if card_info:
                print('\nYou have successfully logged in!\n')
                if logged_in_screen(db_conn,card_info) == '0':
                    print('\nBye!')
                    break
            else:
                print('\nWrong card number or PIN!\n')

def user_login(db_conn):
    card_number = input('Enter your card number:\n')
    pin = input('Enter your PIN:\n')
    db_cur = db_conn.cursor()
    db_cur.execute(f'select number,pin from card where number = "{card_number}" and pin = "{pin}";')
    db_res = db_cur.fetchall()
    if db_res:
        return db_res[0]

def  logged_in_screen(db_conn,card_info):
    card_obj = Card(db_conn,card_info)
    choice = None
    while True:
        print(
'''1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit'''
        )
        user_choice = input('>')
        if user_choice == '1':
            print(f'\nBalance: {card_obj.get_balance()}\n')
        elif user_choice == '5':
            print('\nYou have successfully logged out!\n')
            break
        elif user_choice == '0':
            choice = user_choice
            break
        elif user_choice == '2':
            income_choice = int(input('\nEnter income:\n>'))
            card_obj.add_income(income_choice)
            print('Income was added!\n')
        elif user_choice == '3':
            print('\nTransfer')
            receiver_account = input("Enter card number:\n>")
            print(card_obj.transfer(receiver_account))
        elif user_choice == '4':
            print(card_obj.delete_account())
            break
    return choice

def get_db_info():
    db_conn = sqlite3.connect('card.s3db')
    db_cur = db_conn.cursor()

    db_cur.execute('create table if not exists card(id INTEGER primary key, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);')
    db_conn.commit()

    return db_conn

if __name__ == "__main__":
    db_conn= get_db_info()

    main_screen(db_conn)

"""
Your card number:
4000003051194591
Your card PIN:
8961

Your card has been created
Your card number:
4000005606468321
Your card PIN:
7736

"""