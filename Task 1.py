# Создать программный файл F1 в текстовом формате, записать
# в него построчно данные, вводимые пользователем. Об окончании
# ввода данных будет свидетельствовать пустая строка.
# Скопировать в файл F2 только те строки из F1, которые
# заканчиваются символом «А».
try:
  with open("F1.txt", "w") as file:
    while True:
        line = input("Введите строку для F1 файла: ")
        file.write(line + "\n")
        if not line:
            break
  with open("F1.txt", "r") as f1, open("F2.txt", "w") as f2:
    for line in f1:
        if line.strip().endswith("A"):
         f2.write(line)
         print("Строки с А в конце скопированы!")
finally:
    print("Программа завершилась.")
    with open("F2.txt", "r") as f2:
        f2.read()




