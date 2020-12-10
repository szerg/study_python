from card import Card

def main_screen():
    user_cards = []
    while True:
        print(
'''1. Create an account
2. Log into account
0. Exit''')
        # tine minte s-ar putea sa scoti asta
        user_choice = input('>')
        if user_choice == '0':
            print('\nBye!')
            break
        elif user_choice == '1':
            user_card = Card()
            print(
'''\nYour card has been created
Your card number:\n{}\nYour card PIN:\n{}\n'''.format(user_card.card_number, user_card.pin))
            user_cards.append(user_card)
        elif user_choice == '2':
            if user_login(user_cards):
                print('\nYou have successfully logged in!\n')
                if logged_in_screen() == '0':
                    print('\nBye!')
                    break
            else:
                print('\nWrong card number or PIN!\n')

def user_login(cards):
    card_number = input('Enter your card number:\n')
    pin = input('Enter your PIN:\n')

    for card in  cards:
        if card_number == card.card_number and pin ==card.pin:
            return True
    return False

def  logged_in_screen():
    choice = None
    while True:
        print(
'''1. Balance\n2. Log out\n0. Exit'''
        )
        user_choice = input('>')
        if user_choice == '1':
            print('\nBalance: 0\n')
        elif user_choice == '2':
            print('\nYou have successfully logged out!\n')
            break
        elif user_choice == '0':
            choice = user_choice
            break
    return choice


            
if __name__ == "__main__":
    main_screen()