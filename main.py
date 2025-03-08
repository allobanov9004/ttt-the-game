
from time import sleep
from field import draw_field
from gameplay import player_turn, pc_turn, win_condition

field = [i for i in range(1, 10)]
crosses = []
circles = []




def start_game():
    print("Let's play tic-tac-toe")
    while True:
        draw_field(field, crosses)
        player_turn(field, crosses)

        print("pc's turn")
        if win_condition(crosses):
            draw_field(field, crosses)
            return print("x wins")
        sleep(1)
        pc_turn(field, circles)
        # print(field)
        # print(crosses)
        # print(circles)
        if win_condition(circles):
            draw_field(field, crosses)
            return print("O wins")
        else:
            continue


if __name__ == "__main__":
    start_game()