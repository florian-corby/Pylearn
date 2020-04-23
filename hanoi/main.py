#!/usr/bin/env python3

import time
import sys
import os
import hanoi_solver
import hanoi_ascii
import towers_manipulation
from input_parsers import *


def main_title():
    w, h = os.get_terminal_size()
    print(r"__/\\\________/\\\__________________________________________________        ".center(w))
    time.sleep(0.05)
    print(r" _\/\\\_______\/\\\__________________________________________________       ".center(w))
    time.sleep(0.05)
    print(r"  _\/\\\_______\/\\\_____________________________________________/\\\_      ".center(w))
    time.sleep(0.05)
    print(r"   _\/\\\\\\\\\\\\\\\__/\\\\\\\\\_____/\\/\\\\\\_______/\\\\\____\///__     ".center(w))
    time.sleep(0.05)
    print(r"    _\/\\\/////////\\\_\////////\\\___\/\\\////\\\____/\\\///\\\___/\\\_    ".center(w))
    time.sleep(0.05)
    print(r"     _\/\\\_______\/\\\___/\\\\\\\\\\__\/\\\__\//\\\__/\\\__\//\\\_\/\\\_   ".center(w))
    time.sleep(0.05)
    print(r"      _\/\\\_______\/\\\__/\\\/////\\\__\/\\\___\/\\\_\//\\\__/\\\__\/\\\_  ".center(w))
    time.sleep(0.05)
    print(r"       _\/\\\_______\/\\\_\//\\\\\\\\/\\_\/\\\___\/\\\__\///\\\\\/___\/\\\_ ".center(w))
    time.sleep(0.05)
    print(r"        _\///________\///___\////////\//__\///____\///_____\/////_____\///__".center(w))


def main_menu():
    w, h = os.get_terminal_size()
    vertical_align = "\n" * int(h/8)
    print(vertical_align)
    print("1. Play it super easy".center(w))
    print("2. Play it easy".center(w))
    print("3. Play it casual".center(w))
    print("4. Play it hard".center(w))
    print("5. Play it super hard".center(w))
    print("6. Play it god-like".center(w))
    print("7. Play it Kratos-like".center(w))
    print("")
    print("0. Exit".center(w))
    print("")

    while True:
        user_choice = input()

        try:
            if user_choice in ("1", "2", "3", "4", "5", "6", "7"):
                os.system("clear")
                hanoi_game(user_choice)
                return 0

            elif user_choice in ("n", "N", "0", "non", "Non", "non", "Non", "exit", "Exit"):
                os.system("clear")
                sys.exit(0)

            else:
                raise ValueError

        except ValueError:
            pass


def endgame_menu(towers, difficulty_level, moves_counter):

    towers_size = translate_difficulty_level(difficulty_level)
    expected_moves = 2**towers_size - 1

    w, h = os.get_terminal_size()
    vertical_align = "\n" * int(h/8)
    print(vertical_align)

    print("==========================================================".center(w))
    print("============ Congratulations! You won :D !  ==============".center(w))
    print("==========================================================".center(w))

    print("\n\n")
    print(("You made "
          + str(moves_counter)
          + " moves out of the "
          + str(expected_moves)
          + " minimum move! \n").center(w))

    while True:
        try:
            go_on = input("Do you want to play solution? ".center(w))

            if go_on in ("y", "Y", "o", "O", "yes", "Yes", "oui", "Oui"):
                animation_speed = hanoi_solver.solution_animation_speed(difficulty_level)
                os.system("clear")
                hanoi_solver.play_solution(towers_size, animation_speed)
                break

            elif go_on in ("n", "N", "no", "No", "non", "Non"):
                break

            else:
                raise ValueError

        except ValueError:
            pass

    while True:
        try:
            os.system("clear")
            print(vertical_align*2)
            go_on = input("Do you want to go back to main menu? ".center(w))

            if go_on in ("y", "Y", "o", "O", "yes", "Yes", "oui", "Oui"):
                os.system("clear")
                return 0

            elif go_on in ("n", "N", "no", "No", "non", "Non"):
                os.system("clear")
                sys.exit(0)

            else:
                raise ValueError

        except ValueError:
            pass


def hanoi_game(difficulty_level):

    towers_size = translate_difficulty_level(difficulty_level)

    tower1 = hanoi_solver.create_hanoi_tower(towers_size)
    tower2 = towers_manipulation.create_no_ring_hanoi_tower(towers_size)
    tower3 = towers_manipulation.create_no_ring_hanoi_tower(towers_size)
    towers = [tower1, tower2, tower3]
    win_condition = [] + tower1
    moves_counter = 0

    os.system("clear")
    print("\n")
    hanoi_ascii.print_towers(towers)
    print("")

    while True:

        if towers[1] == win_condition:
            return endgame_menu(towers, difficulty_level, moves_counter)

        user_input = input()

        try:
            if user_input in ("q", "Q", "l", "L", "quit",
                                "Quit", "exit", "Exit", "leave", "Leave"):
                os.system("clear")
                sys.exit(0)

            elif user_input in ("b", "B", "back", "Back", "r", "R", "return"):
                os.system("clear")
                return 0

            elif user_input == "s":
                animation_speed = hanoi_solver.solution_animation_speed(difficulty_level)
                hanoi_solver.play_solution(towers_size, animation_speed)
                os.system("clear")
                print("\n")
                hanoi_ascii.print_towers(towers)
                print("")
                continue

            elif len(user_input) < 2:
                raise ValueError

            user_input = input_parse(user_input)
            res_list = [user_input[0], towers_manipulation.translate_tower_index(user_input[1])]

            if int(res_list[0]) in range(1, towers_size+1) and res_list[1] in (1, 2, 3):
                moves_counter += 1
                towers = towers_manipulation.move_ring(res_list, towers)
                os.system("clear")
                print("\n")
                hanoi_ascii.print_towers(towers)
                print("")

            else:
                raise ValueError

        except ValueError:
            print("Invalid movement!")


def main():

    while True:
        os.system("clear")
        print("")
        main_title()
        print("\n")
        main_menu()
        print("\n")


main()
