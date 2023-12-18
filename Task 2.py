# Создать текстовый файл (не программно).
# Построчно записать фамилии студентов и величину их средних
# баллов за сессию (не менее 10 строк). Определить, кто из
# студентов имеет средний балл от 4 до 6, кто от 6 до 8, а
# кто выше 8, вывести фамилии этих студентов. Вывести на
# экран студента с максимальным средним баллом.
# Пример файла:
# Иванов 4.87
with open("Students.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
for line in lines:
       name, average_score = line.split()
       average_score = float(average_score)
       if 4<= average_score < 6:
          print(name, "имеет средний балл от 4 до 6")
       elif 6<= average_score < 8:
          print(name, "имеет средний балл от 6 до 8")
       elif average_score >= 8:
          print(name, "имеет средний балл выше 6")

max_score_student = max(lines, key=lambda x: float(x.split()[1]))
name, max_score = max_score_student.split()
print("Cтудент с максимальным средним баллом -", max_score_student)


