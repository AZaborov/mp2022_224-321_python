import random

difficulty_level = input("Выберите уровень сложности (1 - детский, 2 - лёгкий, 3 - средний, 4 - сложный): ")
questions_count = int(input("Введите количество вопросов: "))
print()
print("Переведите числа в необходимую систему счисления:")

stats = []

for i in range(questions_count):
    correct_number = 0

    if difficulty_level == '1':
        correct_number = random.randint(0, 7)
    elif difficulty_level == '2':
        correct_number = random.randint(0, 15)
    elif difficulty_level == '3':
        correct_number = random.randint(0, 63)
    elif difficulty_level == '4':
        correct_number = random.randint(0, 255)

    mode = random.choice([10, 16])
    question = str(f"{correct_number:b}")

    if mode == 10:
        question += " dec = "
        answer = input(question)
        if int(answer) == correct_number:
            stats.append('Правильно')
        else:
            stats.append('Неправильно')

    elif mode == 16:
        question += " hex = "
        answer = input(question)
        if int(answer, 16) == correct_number:
            stats.append('Правильно')
        else:
            stats.append('Неправильно')

print(stats)

