# Author: ManpreetSingh Rana, StudentId: 40227463
import os
from grid import MyGrid
import sys

arg1 = sys.argv[1]

if (arg1 != "2" and arg1 != "4" and arg1 != "6"):
    print ("Grid size can only be 2 , 4 or 6. Please retry!")

else:
    grid_size = int(arg1)
    grid_obj = MyGrid(grid_size)
    flag = True
    exit_flag = False
    cheat_flag = False
    win_flag = False
    final_score = 0


    def grid_screen():
        grid_obj.grid_on_display()


    def user_menu():
        print()
        print("--------------------")
        print("|    PEEK-A-BOO    |")
        print("--------------------\n")

        grid_screen()

        print("\n1: Let me select two elements")
        print("2: Uncover one element for me")
        print("3: I give up - reveal the grid")
        print("4: New game")
        print("5: Exit\n")

    def exception_handler():
        input ("Press enter to continue ")
    
    
    while flag:
        if cheat_flag:
            user_menu()
            print("You cheated - Loser!. You're score is 0!")
            cheat_flag = False
            print()
            input("Press enter to start a new game! ")
            grid_obj = MyGrid(grid_size)
            os.system("clear")

        if exit_flag:
            user_menu()
            exit_flag = False
            input("Press enter to start a new game! ")
            grid_obj = MyGrid(grid_size)
            os.system("clear")

        if win_flag:
            user_menu()
            print(f"Oh Happy Day. You've won!! Your score is {final_score}")
            win_flag = False
            print()
            input("Press enter to start a new game! ")
            grid_obj = MyGrid(grid_size)
            os.system("clear")

        user_menu()
        user_selection = input("Select: ")

        try:
            if int(user_selection) < 1 or int(user_selection) > 5:
                print("\nInvalid input! Please enter a valid number between 1 and 5.\n")
                exception_handler()
                os.system("clear")

            elif int(user_selection) == 1:
                rerun_flag = True
                while(rerun_flag):
                    m = input("Enter first cell coordinates (e.g., a0): ")
                    n = input("Enter second cell coordinates (e.g., a0): ")
                    if (len(m) > 2) or (len(n) > 2) or (len(m) <= 1) or (len(n) <= 1):
                        print("Input does not match the allowed length of 2. Please try again.")
                    elif m == n:
                        print("Both the coordinates cannot be same. Please try again. ")
                    else:
                        coord1x = m[1]
                        coord1y = m[0]
                        coord2x = n[1]
                        coord2y = n[0]
                        try:
                            decision, final_score = grid_obj.select_two_elements(coord1x, coord1y, coord2x, coord2y)
                            if decision:
                                win_flag = True
                            rerun_flag = False 
                            os.system("clear")
                        except IndexError:
                            print("Input error: column entry is out of range for this grid. Please try again.")
                            
                        except ValueError:
                            print("Invalid input! Please enter valid coordinates")

            elif int(user_selection) == 2:
                rerun_flag = True
                while(rerun_flag):
                    m = input("Enter cell coordinates (e.g., a0): ")
                    if len(m) > 2 or len(m) < 2:
                        print("Input does not match the allowed length of 2. Please try again.")
                    else:
                        x = m[1]
                        y = m[0]
                        try:
                            decision, final_score = grid_obj.uncover_element(x, y)
                            if decision and final_score == 0:
                                cheat_flag = True
                            elif decision and final_score != 0:
                                win_flag = True
                            rerun_flag = False 
                            os.system("clear")
                        except IndexError:
                            print("Input error: column entry is out of range for this grid. Please try again.")
                        except ValueError:
                            print("Invalid input! Please enter valid coordinates.")

                    

            elif int(user_selection) == 3:
                grid_obj.reveal_grid()
                exit_flag = True
                os.system("clear")

            elif int(user_selection) == 4:
                grid_obj = MyGrid(grid_size)
                os.system("clear")

            elif int(user_selection) == 5:
                print("Thank you for playing this game. See you soon!\n")
                flag = False
            else:
                print(" Please enter a valid choice between 1 and 5.")
                os.system("clear")

        except ValueError:
            print("\nInvalid input! Please enter a valid number between 1 and 5.\n")
            exception_handler()
            os.system("clear")
