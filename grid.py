import random
import time
import os


class MyGrid:

    def __init__(self, size):
        self.display_grid = [['X' for _ in range(size)] for _ in range(size)]
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.grid_size = size
        self.generate_pairs(size)
        self.guess_count = 0
        self.valid_guess_count = 0

    def user_menu(self):
        print()
        print("--------------------")
        print("|    PEEK-A-BOO    |")
        print("--------------------\n")

        self.grid_on_display()

        print("\n1: Let me select two elements")
        print("2: Uncover one element for me")
        print("3: I give up - reveal the grid")
        print("4: New game")
        print("5: Exit\n")

    def generate_pairs(self, size):
        custom_size = int((size * size) / 2)
        n_row = list(range(custom_size))
        n_col = list(range(custom_size))
        merged_list = n_row + n_col
        # Shuffle the numbers randomly
        random.shuffle(merged_list)
        # Assign pairs to the grid
        for i in range(size):
            for j in range(size):
                number = merged_list.pop()
                self.grid[i][j] = number

        return self.grid

    def grid_on_display(self):
        for m in range(self.grid_size + 1):
            for n in range(self.grid_size + 1):
                if m == 0 and n == 0:
                    print("  ", end=" ")

                elif m == 0:
                    char = chr(ord('A') + n - 1)
                    print("[" + char + "]", end=" ")
                elif n == 0:
                    print("[" + str(m - 1) + "]", end=" ")

                else:
                    print(self.display_grid[m - 1][n - 1], end="   ")
            print()

    def uncover_element(self, x, y):
        x = int(x)
        y = ord(str.upper(y)) - ord(str.upper('A'))
        self.display_grid[x][y] = self.grid[x][y]
        self.guess_count += 2
        exit_loop = False
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.display_grid[i][j] == 'X':
                    exit_loop = True
                    break
            if exit_loop:
                break

        if exit_loop:  # if exit loop is true, it means continue normal execution
            return False, 0

        elif (not exit_loop and self.valid_guess_count == 0):
            return True, 0
        else:
            return True, self.score()

    def reveal_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.display_grid[i][j] = self.grid[i][j]

    def select_two_elements(self, coord1x, coord1y, coord2x, coord2y):
        coord1x = int(coord1x)
        coord1y = ord(str.upper(coord1y)) - ord(str.upper('A'))
        coord2x = int(coord2x)
        coord2y = ord(str.upper(coord2y)) - ord(str.upper('A'))
        exit_loop = False
        temp1 = self.display_grid[coord1x][coord1y]
        temp2 = self.display_grid[coord2x][coord2y]
        if self.grid[coord1x][coord1y] == self.grid[coord2x][coord2y]:
            self.display_grid[coord1x][coord1y] = self.grid[coord1x][coord1y]
            self.display_grid[coord2x][coord2y] = self.grid[coord2x][coord2y]
            for i in range(self.grid_size):
                for j in range(self.grid_size):
                    if self.display_grid[i][j] == 'X':
                        exit_loop = True
                        break
                if exit_loop:
                    break

            if exit_loop:
                self.guess_count += 1
                self.valid_guess_count += 1
                return False, 0

            else:
                self.guess_count += 1
                self.valid_guess_count += 1
                return True, self.score()

        else:
            self.display_grid[coord1x][coord1y] = self.grid[coord1x][coord1y]
            self.display_grid[coord2x][coord2y] = self.grid[coord2x][coord2y]
            os.system("clear")
            self.user_menu()
            time.sleep(2)
            os.system("clear")
            self.display_grid[coord1x][coord1y] = temp1
            self.display_grid[coord2x][coord2y] = temp2
            self.guess_count += 1
            self.valid_guess_count += 1
            return False, 0

        

    def score(self):
        min_guess = (self.grid_size * self.grid_size) / 2
        final_score = float(min_guess / self.guess_count) * 100
        return final_score
