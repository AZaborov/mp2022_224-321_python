import random

print(random.randint(0, 100))
print(random.choice(["Один", "Два", "Три", "Четыре", "Пять"]))
print(random.getrandbits(8))
print(random.random())
a = ["яблоко", "банан", "персик"]
random.shuffle(a)
print(a)