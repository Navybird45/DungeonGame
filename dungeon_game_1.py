import random
import os

high_score = [15]
first_place = ["Niel Armstrong"]

CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), ]


def clear_screen():
    """Looks at system;
    Runs 'nt' for all modern versions of Windows;
    Runs 'clear' if on a non-Windows computer;
    """
    os.system("cls" if os.name == "nt" else "clear")


def get_locations():
    """Gets random locations for variables from CELLS"""
    return random.sample(CELLS, 3)


def move_player(player, move):
    """Moves the player along the x or y coordinate based on selected move"""
    x, y = player
    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == "UP":
        y -= 1
    if move == "DOWN":
        y += 1
    return x, y


def get_moves(player):
    """Gives a list of available moves based on player location and walls"""
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    return moves


def draw_map(player, door, monster):
    """Draws the map grid, and places icons for the variables"""
    print(" _" * 5)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            elif cell == door:
                output = tile.format("O")
            elif cell == monster:
                output = tile.format("M")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            elif cell == door:
                output = tile.format("O|")
            elif cell == monster:
                output = tile.format("M|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)


def game_loop():
    """Glabalizes high_score and first_place;
    Gets locations for variables, and shows high score and first place;
    Draws map, gives valid moves, and tells player their location;
    Tells player available movea and waits on an input;
    If player hits monster they lose, door they win;
    nothing they keep playing, if they win or lose they can play again
    """
    global high_score
    global first_place
    player, door, monster = get_locations()
    playing = True
    move_count = 0
    input("""The high score is currently held by {} with a score of {}!
    """.format(first_place[0], high_score[0]))
    clear_screen()

    while playing:
        clear_screen()
        high_score.sort()

        draw_map(player, door, monster)
        valid_moves = get_moves(player)

        print("You're currently in room {}".format(player))
        print("You can move {}".format(", ".join(valid_moves)))
        print("Enter 'QUIT' to quit")

        move = input("> ")
        move = move.upper()
        clear_screen()

        if move == 'QUIT':
            print("\n** See you next time! **\n")
            break
        if move in valid_moves:
            move_count += 1
            player = move_player(player, move)
            clear_screen()
            draw_map(player, door, monster)

            if player == monster:
                print("""
                \n ** Oh no! The monster fot you! Better luck next time **\n
                """)
                playing = False
            if player == door:
                new_high = move_count
                high_score.sort()
                print("""\n** You escaped in {} moves! Congratulations! **\n
                """.format(new_high))
                if new_high < high_score[0]:
                    high_score.insert(0, new_high)
                    print("\n** You have the new high score!!! **\n")
                    first_place[0] = input("What is your name? \n > ")
                else:
                    print("""The high score is still held by {} with a score
                    of {}!""".format(first_place[0], high_score[0]))
                playing = False
        else:
            input("\n ** Walls are hard! Don't run into them! **\n")
    else:
        if input("Play again? [Y/n]").lower != "n":
            game_loop()


if __name__ == '__main__':
    """Only runs script if being ran from file, not imported as method"""
    clear_screen()
    print("Welcome to the dungeon!")
    input("Press return to start!")
    clear_screen
    game_loop()
