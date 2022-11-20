width = int(input("Ширина: "))
height = int(input("Высота: "))
print()

route = []
for i in range(height):
    row = []
    for j in range(width):
        row.append(" ")
    route.append(row)

x = 0
y = 0


def move_right():
    global x
    x += 1


def move_left():
    global x
    x -= 1


def move_up():
    global y
    y -= 1


def move_down():
    global y
    y += 1


def draw():
    route[y][x] = "█"


if __name__ == "__main__":
    i = 0
    while not route[y][x] == "█":
        while x < width - 1 - 2 * i:
            draw()
            move_right()
        while y < height - 1 - 2 * i:
            draw()
            move_down()
        while x > 0 + 2 * i:
            draw()
            move_left()
        while y > 2 + 2 * i:
            draw()
            move_up()
        i += 1

    for iy in range(height):
        for ix in range(width):
            print(route[iy][ix], end=" ")
        print()
