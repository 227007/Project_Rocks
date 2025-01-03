import random

class Player:
    def __init__(self, name):
        self.name = name
        self.move = None

    def choose_move(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def __str__(self):
        return f"{self.name} chose {self.move}"

class HumanPlayer(Player):
    def choose_move(self):
        valid_moves = ["rock", "paper", "scissors"]
        while True:
            self.move = input("Enter your move (rock, paper, scissors): ").lower()
            if self.move in valid_moves:
                break
            else:
                print("Invalid move. Please choose again.")

class AlwaysRockPlayer(Player):
    def choose_move(self):
        self.move = "rock"

class RandomPlayer(Player):
    def choose_move(self):
        self.move = random.choice(["rock", "paper", "scissors"])

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.scores = {player1.name: 0, player2.name: 0}

    def play_round(self):
        self.player1.choose_move()
        self.player2.choose_move()
        print(self.player1)
        print(self.player2)
        self.determine_winner()

    def determine_winner(self):
        beats = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
        if self.player1.move == self.player2.move:
            print("It's a tie!")
        elif beats[self.player1.move] == self.player2.move:
            print(f"{self.player1.name} wins this round!")
            self.scores[self.player1.name] += 1
        else:
            print(f"{self.player2.name} wins this round!")
            self.scores[self.player2.name] += 1

    def play_game(self, rounds=3):
        for _ in range(rounds):
            self.play_round()
            print(f"Scores: {self.scores}")
        print("Game over!")

# Example gameplay
player1 = HumanPlayer("You")
player2 = RandomPlayer("Computer")
game = Game(player1, player2)
game.play_game()
