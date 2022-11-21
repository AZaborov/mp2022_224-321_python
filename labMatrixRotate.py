import random

MATRIX_WIDTH = 5
MATRIX_HEIGHT = 5
MATRIX = []


def fill_matrix():
    for _ in range(MATRIX_HEIGHT):
        row = []
        for _ in range(MATRIX_WIDTH):
            row.append(random.randint(10, 99))
        MATRIX.append(row)


def print_matrix():
    for y in range(MATRIX_HEIGHT):
        for x in range(MATRIX_WIDTH):
            print(MATRIX[x][y], end=' ')
        print()


def rotate_left():
    global MATRIX
    h, w = len(MATRIX), len(MATRIX[0])
    new_array = [[None] * h for _ in range(w)]
    for c in range(w - 1, -1, -1):
        for r in range(h):
            new_array[c][h - r - 1] = MATRIX[r][c]
    MATRIX = new_array.copy()


def rotate_right():
    global MATRIX
    h, w = len(MATRIX), len(MATRIX[0])
    new_array = [[None] * h for _ in range(w)]
    for c in range(w):
        for r in range(h - 1, -1, -1):
            new_array[w - c - 1][r] = MATRIX[r][c]
    MATRIX = new_array.copy()


def mirror():
    global MATRIX
    h, w = len(MATRIX), len(MATRIX[0])
    new_array = [[None] * h for _ in range(w)]
    for c in range(w):
        for r in range(h):
            new_array[r][c] = MATRIX[w - r - 1][c]
    MATRIX = new_array.copy()


if __name__ == "__main__":
    fill_matrix()
    print_matrix()

    while True:
        command = input("Введите команду (a - повернуть налево, d - повернуть направо, s - отразить): ")

        if command == 'A' or command == 'a':
            rotate_left()
            print_matrix()
        elif command == 'D' or command == 'd':
            rotate_right()
            print_matrix()
        elif command == 'S' or command == 's':
            mirror()
            print_matrix()
