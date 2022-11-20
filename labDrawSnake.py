width = int(input("Ширина: "))
height = int(input("Высота: "))
odd_lines_count = 0
print()

for i in range(height):
    if i % 2 == 0:
        for j in range(width):
            print("█", end="")
    else:
        if odd_lines_count % 2 == 0:
            print(" " * (width - 1) + "█", end="")
        else:
            print("█", end="")
        odd_lines_count += 1
    print()
