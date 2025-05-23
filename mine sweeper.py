import random

class Minesweeper:
    def __init__(self, rows, cols, num_mines):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self._place_mines()
        self._calculate_adjacent()

    def _place_mines(self):
        mines_placed = 0
        while mines_placed < self.num_mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            if self.board[r][c] != 'M':
                self.board[r][c] = 'M'
                mines_placed += 1

    def _calculate_adjacent(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == 'M':
                    continue
                count = 0
                for i in range(max(0, r - 1), min(self.rows, r + 2)):
                    for j in range(max(0, c - 1), min(self.cols, c + 2)):
                        if self.board[i][j] == 'M':
                            count += 1
                self.board[r][c] = str(count)

    def reveal(self, r, c):
        if self.revealed[r][c]:
            return
        self.revealed[r][c] = True
        if self.board[r][c] == 'M':
            print("Game Over! You hit a mine.")
            self.show_board(reveal_all=True)
            exit()
        elif self.board[r][c] == '0':
            for i in range(max(0, r - 1), min(self.rows, r + 2)):
                for j in range(max(0, c - 1), min(self.cols, c + 2)):
                    if not self.revealed[i][j]:
                        self.reveal(i, j)

    def show_board(self, reveal_all=False):
        print("   " + " ".join([str(i) for i in range(self.cols)]))
        print("  +" + "--" * self.cols + "+")
        for r in range(self.rows):
            row_str = f"{r} |"
            for c in range(self.cols):
                if reveal_all or self.revealed[r][c]:
                    row_str += self.board[r][c] + " "
                else:
                    row_str += "# "
            row_str += "|"
            print(row_str)
        print("  +" + "--" * self.cols + "+")

    def check_win(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] != 'M' and not self.revealed[r][c]:
                    return False
        return True

def main():
    game = Minesweeper(rows=5, cols=5, num_mines=5)

    while True:
        game.show_board()
        try:
            r = int(input("Enter row: "))
            c = int(input("Enter column: "))
            if 0 <= r < game.rows and 0 <= c < game.cols:
                game.reveal(r, c)
                if game.check_win():
                    print("Congratulations! You won!")
                    game.show_board(reveal_all=True)
                    break
            else:
                print("Invalid coordinates.")
        except ValueError:
            print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
