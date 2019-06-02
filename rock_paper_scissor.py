import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumenPlayer(Player):
    def move(self):
        while True:
            self.Humen = input("choose rock, paper or scissors: ")
            if self.Humen in moves:
                break
        return self.Humen


class ReflectPlyer(Player):
    reflect_move = 'rock'

    def move(self):
        return self.reflect_move

    def learn(self, my_move, their_move):
        self.reflect_move = their_move


class cyclePlayer(Player):
    cycle_move = 'rock'

    def move(self):
        return self.cycle_move

    def learn(self, my_move, their_move):
        if my_move == 'rock':
            self.cycle_move = 'paper'
        elif my_move == 'paper':
            self.cycle_move = 'scissors'
        elif my_move == 'scissors':
            self.cycle_move = 'rock'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

        self.p1.score = 0
        self.p2.score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.p1.score = self.p1.score + 1
        elif beats(move2, move1):
            self.p2.score = self.p2.score + 1


        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print("Player 1: ", self.p1.score, "Player 2: ", self.p2.score)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()

        print("score: ", self.p1.score, "-", self.p2.score)
        if self.p1.score > self.p2.score:
            print("Player 1 WON")
        elif self.p1.score < self.p2.score:
            print("Player 2 WON ")
        else:
            print("It is a Tie")

        play_again = input(print("Do you want to play agin ? Yes or No "))
        if play_again == 'yes':
            play()
        else:
            print("Game over!")


def play():
    if __name__ == '__main__':
        game = Game(HumenPlayer(), RandomPlayer())
        game.play_game()


play()
