import pygame

pygame.init()
WIDTH = 500
HEIGHT = 450
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Gentlemen\'s Chess')
font = pygame.font.Font('freesansbold.ttf', 10)
medium_font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 25)
timer = pygame.time.Clock()
fps = 60

# asset import and piece setup
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []
# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
turn_step = 0
selection = 100
valid_moves = []
# load in game piece images (queen, king, rook, bishop, knight, pawn) x 2 (white and black)
black_queen = pygame.image.load('assets/Chess_qdt60.png')
black_queen = pygame.transform.scale(black_queen, (40, 40))
black_queen_small = pygame.transform.scale(black_queen, (22, 22))
black_king = pygame.image.load('assets/Chess_kdt60.png')
black_king = pygame.transform.scale(black_king, (40, 40))
black_king_small = pygame.transform.scale(black_king, (22, 22))
black_rook = pygame.image.load('assets/Chess_rdt60.png')
black_rook = pygame.transform.scale(black_rook, (40, 40))
black_rook_small = pygame.transform.scale(black_rook, (22, 22))
black_bishop = pygame.image.load('assets/Chess_bdt60.png')
black_bishop = pygame.transform.scale(black_bishop, (40, 40))
black_bishop_small = pygame.transform.scale(black_bishop, (22, 22))
black_knight = pygame.image.load('assets/Chess_ndt60.png')
black_knight = pygame.transform.scale(black_knight, (40, 40))
black_knight_small = pygame.transform.scale(black_knight, (22, 22))
black_pawn = pygame.image.load('assets/Chess_pdt60.png')
black_pawn = pygame.transform.scale(black_pawn, (32, 32))
black_pawn_small = pygame.transform.scale(black_pawn, (22, 22))
white_queen = pygame.image.load('assets/Chess_qlt60.png')
white_queen = pygame.transform.scale(white_queen, (40, 40))
white_queen_small = pygame.transform.scale(white_queen, (22, 22))
white_king = pygame.image.load('assets/Chess_klt60.png')
white_king = pygame.transform.scale(white_king, (40, 40))
white_king_small = pygame.transform.scale(white_king, (22, 22))
white_rook = pygame.image.load('assets/Chess_rlt60.png')
white_rook = pygame.transform.scale(white_rook, (40, 40))
white_rook_small = pygame.transform.scale(white_rook, (22, 22))
white_bishop = pygame.image.load('assets/Chess_blt60.png')
white_bishop = pygame.transform.scale(white_bishop, (40, 40))
white_bishop_small = pygame.transform.scale(white_bishop, (22, 22))
white_knight = pygame.image.load('assets/Chess_nlt60.png')
white_knight = pygame.transform.scale(white_knight, (40, 40))
white_knight_small = pygame.transform.scale(white_knight, (22, 22))
white_pawn = pygame.image.load('assets/Chess_plt60.png')
white_pawn = pygame.transform.scale(white_pawn, (32, 32))
white_pawn_small = pygame.transform.scale(white_pawn, (22, 22))
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']


# in game functions
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, "white", [300 - (column * 100), row * 50, 50, 50])
        else:
            pygame.draw.rect(screen, "white", [350 - (column * 100), row * 50, 50, 50])

        pygame.draw.rect(screen, "black", [0, 400, WIDTH, 50])
        pygame.draw.rect(screen, "dark gray", [400, 0, 100, HEIGHT])
        pygame.draw.rect(screen, "black", [0, 400, WIDTH, 50], 5)
        pygame.draw.rect(screen, "black", [400, 0, 100, HEIGHT], 5)
        pygame.draw.rect(screen, "maroon", [405, 405, 90, 40])

        status_text = ['White\'s turn: Select a Piece', 'White\'s turn: Select a Destination',
                       'Black\'s turn: Select a Piece', 'Black\'s turn: Select a Destination']
        screen.blit(medium_font.render(status_text[turn_step], True, 'white'), (20, 415))


def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == "pawn":
            screen.blit(white_pawn, (white_locations[i][0] * 50 + 7, white_locations[i][1] * 50 + 7))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 50 + 4, white_locations[i][1] * 50 + 4))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * 50, white_locations[i][1] * 50,
                                                 50, 50], 2)
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == "pawn":
            screen.blit(black_pawn, (black_locations[i][0] * 50 + 7, black_locations[i][1] * 50 + 7))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 50 + 4, black_locations[i][1] * 50 + 4))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 50, black_locations[i][1] * 50,
                                                  50, 50], 2)


def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        else:
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)

    return all_moves_list


def check_knight(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list


def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list


def check_valid_moves():
    pass


def draw_valid():
    pass


# main game logic
run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 50
            y_coord = event.pos[1] // 50
            click_coord = (x_coord, y_coord)
            if turn_step < 2:
                if click_coord in white_locations:
                    selection = white_locations.index(click_coord)
                    if turn_step == 0:
                        turn_step = 1
                if click_coord in valid_moves and selection != 100:
                    white_locations[selection] = click_coord
                    if click_coord in black_locations:
                        black_piece = black_locations.index(click_coord)
                        captured_pieces_white.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []

            if turn_step >= 2:
                if click_coord in black_locations:
                    selection = black_locations.index(click_coord)
                    if turn_step == 2:
                        turn_step = 3
                if click_coord in valid_moves and selection != 100:
                    black_locations[selection] = click_coord
                    if click_coord in white_locations:
                        white_piece = white_locations.index(click_coord)
                        captured_pieces_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []

    pygame.display.flip()
pygame.quit()

