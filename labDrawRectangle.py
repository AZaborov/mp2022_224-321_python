def draw():
    for i in range(height):
        for j in range(width):
            if is_painted == "y" or i == 0 or i == height - 1 or j == 0 or j == width - 1:
                print(symbol, end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":
    width = int(input("Ширина: "))
    height = int(input("Высота: "))
    symbol = input("Символ рисования: ")
    is_painted = input("Закрасить фигуру? (y/n): ")
    print()
    draw()
    is_continued = input("Повторить? (y/n): ")
    if is_continued == "y":
        print()
        draw()
