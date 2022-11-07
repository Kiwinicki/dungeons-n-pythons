import os
import msvcrt

from Map import Map


def main():
    map = Map(size=(5, 5), player_pos=(0, 0), apple_pos=(4, 4))

    while True:
        print('--- Dungeons & Pythons --- ')
        print('oznaczenia: P - Gracz, O - Cel, R - Skała, D - Pułapka')
        print('sterowanie: WSAD, wyjście: q')
        map.draw_map()

        # check win condition
        if map.apple_pos == map.player_pos:
            break

        # wait for key
        key = ''
        while True:
            key = msvcrt.getwch().upper()

            if key in ['W', 'S', 'A', 'D']:
                break
            if key == 'Q':  # quit program
                return True

        # change player position
        map.move_player(key)

        # clear console window
        if os.name == 'nt':
            os.system('cls')  # for windows
        else:
            os.system('clear')  # for linux


if __name__ == "__main__":
    main()
