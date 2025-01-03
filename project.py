import random

# Constants for moves
MOVES = ["rock", "paper", "scissors"]

class Player:
    """Base player class."""
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def remember(self, opponent_move):
        pass  # Default behavior: do nothing

class AlwaysRockPlayer(Player):
    """Player that always plays 'rock'."""
    def move(self):
        return "rock"

    def remember(self, opponent_move):
        pass

class RandomPlayer(Player):
    """Player that chooses moves randomly."""
    def move(self):
        return random.choice(MOVES)

    def remember(self, opponent_move):
        pass

class ImitatorPlayer(Player):
    """Player that imitates the human's previous move."""
    def __init__(self):
        self.last_opponent_move = None

    def move(self):
        return self.last_opponent_move or random.choice(MOVES)

    def remember(self, opponent_move):
        self.last_opponent_move = opponent_move

class CyclicPlayer(Player):
    """Player that cycles through the three moves."""
    def __init__(self):
        self.index = 0

    def move(self):
        move = MOVES[self.index]
        self.index = (self.index + 1) % len(MOVES)
        return move

    def remember(self, opponent_move):
        pass

class HumanPlayer(Player):
    """Human player class."""
    def move(self):
        while True:
            user_move = input(f"Enter your move ({', '.join(MOVES)}): ").lower()
            if user_move in MOVES:
                return user_move
            print("Invalid move. Please try again.")

    def remember(self, opponent_move):
        pass

def determine_winner(move1, move2):
    """Determine the winner based on moves."""
    if move1 == move2:
        return "tie"
    if (move1 == "rock" and move2 == "scissors") or \
       (move1 == "scissors" and move2 == "paper") or \
       (move1 == "paper" and move2 == "rock"):
        return "player1"
    return "player2"

class Game:
    """Rock Paper Scissors Game class."""
    def __init__(self, player1, player2, rounds=3):
        self.player1 = player1
        self.player2 = player2
        self.rounds = rounds
        self.scores = {"player1": 0, "player2": 0, "tie": 0}

    def play_round(self):
        """Play a single round."""
        move1 = self.player1.move()
        move2 = self.player2.move()

        print(f"Player 1 played: {move1}")
        print(f"Player 2 played: {move2}")

        winner = determine_winner(move1, move2)
        if winner != "tie":
            print(f"{winner.capitalize()} wins this round!")
        else:
            print("It's a tie!")

        self.scores[winner] += 1

        self.player1.remember(move2)
        self.player2.remember(move1)

    def play_match(self):
        """Play a match consisting of multiple rounds."""
        print(f"Starting a match of {self.rounds} rounds!\n")
        for round_number in range(1, self.rounds + 1):
            print(f"Round {round_number}:")
            self.play_round()
            print(f"Scores: {self.scores}\n")
        print("Final Scores:")
        print(self.scores)

        if self.scores["player1"] > self.scores["player2"]:
            print("Player 1 is the overall winner!")
        elif self.scores["player1"] < self.scores["player2"]:
            print("Player 2 is the overall winner!")
        else:
            print("The match is a tie!")

if __name__ == "__main__":
    print("Welcome to Rock Paper Scissors!")
    human = HumanPlayer()
    computer = RandomPlayer()  # You can replace this with any other computer strategy
    game = Game(human, computer, rounds=5)
    game.play_match()
