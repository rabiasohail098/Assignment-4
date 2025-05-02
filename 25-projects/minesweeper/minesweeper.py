import random
import re

class Board:
    def __init__(self, dim_size, num_bomb):
        self.dim_size = dim_size
        self.num_bomb = num_bomb
        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set()

    def make_new_board(self):
        """Create a new board and randomly place bombs."""
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        
        bombs_planted = 0
        while bombs_planted < self.num_bomb:
            loc = random.randint(0, self.dim_size**2 - 1) 
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':  # If bomb is already placed, continue
                continue

            board[row][col] = '*'  # Place bomb
            bombs_planted += 1

        return board  

    def assign_values_to_board(self):
        """Assign numbers to board indicating how many bombs are nearby."""
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        """Count the number of bombs surrounding a given square."""
        num_neighboring_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        return num_neighboring_bombs

    def dig(self, row, col):
        """Recursively dig up board if it's safe."""
        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)

        return True

    def __str__(self):
        """Return a string representation of the board with grid lines."""
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        board_str = "\n"
        header = "   " + " | ".join(str(i) for i in range(self.dim_size))  # Column numbers
        board_str += header + "\n" + "-" * (4 * self.dim_size) + "\n"

        for i, row in enumerate(visible_board):
            board_str += str(i) + " | " + " | ".join(row) + " |\n"  # Row numbers
            board_str += "-" * (4 * self.dim_size) + "\n"

        return board_str


def play(dim_size=10, num_bombs=10):
    """Start the game with given board size and number of bombs."""
    board = Board(dim_size, num_bombs)
    print("\n🚀 Welcome to Minesweeper! 🚀")
    print(f"💣 There are {num_bombs} bombs hidden in a {dim_size}x{dim_size} grid.\n")
    
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        print("📌 Enter your move in 'row,col' format. Example: 2,3\n")
        
        user_input = input("👉 Where would you like to dig? ")

        if user_input.lower() == "exit":
            print("\n👋 Exiting game. See you next time!\n")
            return

        try:
            row, col = map(int, re.split(',\\s*', user_input))
            if row < 0 or row >= board.dim_size or col < 0 or col >= board.dim_size:
                print("\n❌ Invalid move! Please enter a valid row and column.\n")
                continue
        except (ValueError, IndexError):
            print("\n❌ Invalid input! Enter in 'row,col' format. Example: 2,3\n")
            continue

        safe = board.dig(row, col)
        
        if not safe:
            print("\n💥 BOOM! You hit a bomb! GAME OVER! 💥\n")
            board.dug = {(r, c) for r in range(board.dim_size) for c in range(board.dim_size)}
            print(board)
            break
        
        print("\n✅ Safe move! Keep going!\n")

    if len(board.dug) == board.dim_size ** 2 - num_bombs:
        print("\n🎉 CONGRATULATIONS! YOU WON! 🎉\n")
    else:
        print("\n😢 Better luck next time! 😢\n")


# ✅ Run the game in a loop until the player decides to quit
if __name__ == "__main__":
    while True:
        play()
        replay = input("🔄 Do you want to play again? (yes/no): ").lower()
        if replay not in ["yes", "y"]:
            print("\n👋 Thanks for playing! Goodbye!\n")
            break
