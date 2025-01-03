import random

# Base player class
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def move(self):
        pass

    def remember(self, my_move, opponent_move):
        pass


# Human player class
class Human(Player):
    def move(self):
        while True:
            choice = input("Enter your move (rock, paper, scissors): ").lower()
            if choice in ["rock", "paper", "scissors"]:
                return choice
            print("Invalid move. Try again!")


# Always plays rock
class AlwaysRock(Player):
    def move(self):
        return "rock"


# Plays randomly
class RandomPlayer(Player):
    def move(self):
        return random.choice(["rock", "paper", "scissors"])


# Imitates the human player's previous move
class Imitator(Player):
    def __init__(self, name):
        super().__init__(name)
        self.last_human_move = "rock"  # Default first move

    def move(self):
        return self.last_human_move

    def remember(self, my_move, opponent_move):
        self.last_human_move = opponent_move


# Cycles through moves
class Cycler(Player):
    def __init__(self, name):
        super().__init__(name)
        self.moves = ["rock", "paper", "scissors"]
        self.index = 0

    def move(self):
        choice = self.moves[self.index]
        self.index = (self.index + 1) % len(self.moves)
        return choice


# Game class
class Game:
    def __init__(self, rounds):
        self.rounds = rounds
        self.human = Human("Human")
        self.computer = None

    def set_computer_player(self, computer_player):
        self.computer = computer_player

    def play_round(self):
        human_move = self.human.move()
        computer_move = self.computer.move()

        print(f"\n{self.human.name} plays: {human_move}")
        print(f"{self.computer.name} plays: {computer_move}")

        if human_move == computer_move:
            print("It's a tie!")
        elif (human_move == "rock" and computer_move == "scissors") or \
             (human_move == "scissors" and computer_move == "paper") or \
             (human_move == "paper" and computer_move == "rock"):
            print(f"{self.human.name} wins this round!")
            self.human.score += 1
        else:
            print(f"{self.computer.name} wins this round!")
            self.computer.score += 1

        self.human.remember(human_move, computer_move)
        self.computer.remember(computer_move, human_move)

    def play_match(self):
        print("\nStarting the match!")
        for round_number in range(1, self.rounds + 1):
            print(f"\n--- Round {round_number} ---")
            self.play_round()
            print(f"\nScores: {self.human.name}: {self.human.score}, {self.computer.name}: {self.computer.score}")

        print("\n--- Final Results ---")
        print(f"{self.human.name}: {self.human.score}")
        print(f"{self.computer.name}: {self.computer.score}")
        if self.human.score > self.computer.score:
            print(f"{self.human.name} wins the match!")
        elif self.human.score < self.computer.score:
            print(f"{self.computer.name} wins the match!")
        else:
            print("The match is a tie!")


if __name__ == "__main__":
    print("Welcome to Rock Paper Scissors!")
    num_rounds = int(input("Enter the number of rounds: "))

    game = Game(num_rounds)

    print("\nChoose a computer player strategy:")
    print("1. Always plays rock")
    print("2. Plays randomly")
    print("3. Imitates your previous move")
    print("4. Cycles through moves")

    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        game.set_computer_player(AlwaysRock("Computer"))
    elif choice == 2:
        game.set_computer_player(RandomPlayer("Computer"))
    elif choice == 3:
        game.set_computer_player(Imitator("Computer"))
    elif choice == 4:
        game.set_computer_player(Cycler("Computer"))
    else:
        print("Invalid choice. Exiting.")
        exit()

    game.play_match()