import random, time

class gamemain:
    rps_dict = {'1':'rock','2':'paper','3':'scissors'}
    score = 0
    turns = 0
    def draw(self):
        print('This round was a draw. \n')
    
    def win(self):
        self.score += 1
        print('Player won this round. \n')
    
    def lose(self):
        self.score -= 1
        print('Player lost this round. \n')

    def start(self):
        while self.turns < 3:
            self.turn(self)

        print('Score of the player : {} \n'.format(self.score))

        if self.score >= 2:
            print("Player won the match! \n")
        elif(self.score == 0):
            print("This match was a tie. \n")
        else:
            print("Player lost the match. \n")

    def turn(self):
        user_play = int(input("enter your move:"))
        comp_play = random.randint(1, 3)

        print("Player drew {}.".format(self.rps_dict[str(user_play)]))
        print("Computer drew {}.".format(self.rps_dict[str(comp_play)]))
        self.turns += 1
        time.sleep(2)

        if(comp_play == user_play):
            self.draw(self)
        elif(user_play - comp_play == 1 or user_play - comp_play <-1):
            self.win(self)
        elif(user_play - comp_play > 1 or user_play - comp_play == -1):
            self.lose(self)


if __name__ == "__main__":
    game = gamemain
    game.start(game)
