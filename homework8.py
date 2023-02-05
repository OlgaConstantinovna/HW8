
import random
# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу. 
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.

def zadacha1():
    group_count = 4

    marks =[0]* group_count

    for i in range(group_count):
        marks[i] = [random.randint(2,5) for _ in range(random.randint(20,30))]

    for row in marks:
        print(row)    

    mark_max = 0
    group_max = 0

    for i in range(group_count):
        average_mark = 0
        student_count = len(marks[i])
        for j in range(student_count):
            average_mark += marks[i][j]
        average_mark /= student_count
        if average_mark > mark_max:
            mark_max = average_mark
            group_max = i + 1
            

    print(f'максимальный средний бал у группы {group_max}')  
    print(f' максимальный бал рвен {mark_max}')          
# zadacha1()