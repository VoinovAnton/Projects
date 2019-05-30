import random


class Slot:

    def __init__(self, name, balance):
        self.player_name = name
        self.player_balance = balance

    def fun(self, bet):

        player_number = int(input('Enter number from 1 to 5: '))
        slot_number = random.randint(1, 5)
        print('Slot number:', slot_number)
        if player_number == slot_number:
            self.player_balance += 10
            print('You Win!!! Your balance:', self.player_balance)
        else:
            self.player_balance -= bet
            print('You Lose!!! Your balance:', self.player_balance)


player_age = 18
if player_age >= 18:
    player_name = str(input('Enter your name: '))
    player_balance = int(input('Enter cash: '))
    slot = Slot(player_name, player_balance)
    player_bet = 10
    while slot.player_balance > 0:
        slot.fun(player_bet)
    else:
        print(player_name + ' you have no more money!!!')
else:
    print("Go play in the sandbox!!!")