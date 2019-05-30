import random


class Slot:
    def __init__(self, balance):
        self.player_balance = balance

    def possible_bet(self):
        bets = {'100': 100, '50': 50, '25': 25, '10': 10, '5': 5, '3': 3, '1': 1}
        self.pos_bets = []
        for bet in bets:
            if bets[bet] <= self.player_balance:
                self.pos_bets.append(bets[bet])
        return self.pos_bets

    def input_bet(self):
        print('Select a Bet:', self.pos_bets)
        self.player_bet = int(input("Enter Bet: "))
        if self.player_bet in self.pos_bets:
            self.reels()
            return self.player_bet
        else:
            print('Incorrect Bet!')
            return self.input_bet()

    def reels(self):
        self.reel1 = [1, 2, 3, 4, 5, 6, 7, 8]
        self.reel2 = [1, 2, 3, 4, 5, 6, 7, 8]
        self.reel3 = [1, 2, 3, 4, 5, 6, 7, 8]
        self.convert_id_to_char()

    def shuffle_id(self, reel):
        id_index_reels = []
        rnd = random.randint(0, len(reel) - 1)
        counter = 0
        for id_index, symbol in enumerate(reel):
            if id_index == rnd:
                while counter < 3:
                    counter += 1
                    id_index += 1
                    if id_index > len(reel) - 1:
                        id_index -= len(reel)
                    id_index_reels.append(id_index)
                return id_index_reels

    def convert_id_to_char(self):
        reel_lst1 = []
        reel_lst2 = []
        reel_lst3 = []
        self.char_reel1 = self.shuffle_id(self.reel1)
        self.char_reel2 = self.shuffle_id(self.reel2)
        self.char_reel3 = self.shuffle_id(self.reel3)
        for i in self.char_reel1:
            reel_lst1.append(self.reel1[i])
        for i in self.char_reel2:
            reel_lst2.append(self.reel2[i])
        for i in self.char_reel3:
            reel_lst3.append(self.reel3[i])
        self.lines(reel_lst1, reel_lst2, reel_lst3)

    def lines(self, reel1, reel2, reel3):
        reels = [reel1, reel2, reel3]
        print(reels)
        self.counter = 0
        if reels[0][0] == reels[1][0]:
            self.counter += 1
        if reels[0][1] == reels[1][1]:
            self.counter += 1
        if reels[0][2] == reels[1][2]:
            self.counter += 1
        else:
            pass
        self.spin()

    def spin(self):
        if self.counter > 0:
            self.player_balance += self.counter * self.player_bet
            print('You Win!!!, Balance:', self.player_balance)
            self.possible_bet()
            self.input_bet()
            return self.player_balance
        else:
            self.player_balance -= self.player_bet
            print('You Lose!!!, Balance:', self.player_balance)
            if self.player_balance > 0:
                self.possible_bet()
                self.input_bet()
                return self.player_balance
            else:
                return self.player_balance


credit = int(input('Enter cash: '))
if credit > 0:
    slot = Slot(credit)
    slot.possible_bet()
    slot.input_bet()
else:
    print('Enter the correct number of credits')