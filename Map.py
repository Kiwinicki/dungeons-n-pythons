class Map:
    def __init__(self, size: tuple, player_pos: tuple, apple_pos: tuple):
        self.size = size  # (cols, rows)
        self.player_pos = player_pos  # (x, y)
        self.apple_pos = apple_pos  # (x, y)

    def draw_map(self):
        (cols, rows) = self.size

        print('╔' + '═'*(cols*2) + '╗')

        for y in range(rows):
            print('║', end='')
            for x in range(cols):
                if self.player_pos[0] == x and self.player_pos[1] == y:
                    print('P ', end='')
                elif self.apple_pos[0] == x and self.apple_pos[1] == y:
                    print('O ', end='')
                else:
                    print('. ', end='')
            print('║')

        print('╚' + '═'*(cols*2) + '╝')

    def move_player(self, key):
        (x, y) = self.player_pos
        match key:
            case 'W':
                if y > 0:
                    self.player_pos = (x, y - 1)
            case 'S':
                if y < self.size[1] - 1:
                    self.player_pos = (x, y + 1)
            case 'A':
                if x > 0:
                    self.player_pos = (x - 1, y)
            case 'D':
                if x < self.size[0] - 1:
                    self.player_pos = (x + 1, y)
            case _:
                pass
