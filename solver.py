from polyomino.constant import MONOMINO
from polyomino.board import Rectangle
from polyomino.tileset import Tileset


def rectangle_polyomino_by_size(rectangle_size):
    width, height = rectangle_size
    rectangle_polyomino = []
    for curr_width in range(width):
        for curr_height in range(height):
            rectangle_polyomino.append([curr_width, curr_height])
    return rectangle_polyomino


def l_polyomino_by_size(l_size):
    width, height = l_size
    l_polyomino = []
    for curr_width in range(width):
        l_polyomino.append([curr_width, 0])
    for curr_height in range(1, height):
        l_polyomino.append([0, curr_height])
    return l_polyomino


def polyomino_solver(board_size, rectangle_polyominos, l_polyominos):
    board = Rectangle(board_size[0], board_size[1])
    tileset = Tileset([], [], [])
    board_square, used_square = board_size[0] * board_size[1], 0
    for rectangle_polyomino in rectangle_polyominos:
        width, height = rectangle_polyomino[0]
        count = rectangle_polyomino[1]
        used_square += count * width * height
        curr_polyomino = rectangle_polyomino_by_size((width, height))
        tileset = tileset.and_repeated_exactly(count, curr_polyomino)
    for l_polyomino in l_polyominos:
        width, height = l_polyomino[0]
        count = l_polyomino[1]
        used_square += count * (width + height - 1)
        curr_polyomino = l_polyomino_by_size((width, height))
        tileset = tileset.and_repeated_exactly(count, curr_polyomino)
    if used_square > board_square:
        return False

    return board.tile_with_set(tileset.and_repeated_exactly(
        board_square - used_square, MONOMINO)) is not None
