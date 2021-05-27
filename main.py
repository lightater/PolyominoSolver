from solver import polyomino_solver

if __name__ == '__main__':
    BoardSize = (5, 5)
    RectanglePolyominos = [((2, 2), 2)]
    LPolyominos = [((3, 2), 1), ((2, 2), 2)]
    print(polyomino_solver(BoardSize, RectanglePolyominos, LPolyominos))
