
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

# Задача 2. Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.
def zadacha2():

    rows = 4
    numbers =[0]* rows

    for i in range(rows):
        numbers[i] = [random.randint(1, 100) for _ in range(rows)]

    for row in numbers:
        print(row)    

    diagonal_sum = 0
    for i in range(rows):
        diagonal_sum += numbers[i][i]
    # print(f'сумма элементов главной диагонали равна { diagonal_sum}')

    for index in range(len(numbers)):
        sum_in_row = sum(numbers[index])
        if sum_in_row > diagonal_sum:
            print(f'в строке {index+1}, сумма элементов {numbers[index]} = {sum_in_row} превышает сумму элементов ГД {diagonal_sum}')   

# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. Каждому месяцу соответствует своя строка.
# Определите самый жаркий и самый холодный 7-дневный промежуток каждого месяца. Выведите их даты.
def period_for_mounth(temperature_in_mounth, period, mounth):
    max_temp = 0
    day_max_temp = 1
    min_temp = 1000
    day_min_temp = 1
 
    for day in range(len(temperature_in_mounth) - period + 1):
        temp_in_period = temperature_in_mounth[day:day + period]
        sum_temp_in_period = sum(temp_in_period)
        print(f'{day + 1} - {day + period} {temp_in_period}')
        if sum_temp_in_period >  max_temp:
            max_temp = sum_temp_in_period
            day_max_temp = day
        elif sum_temp_in_period < min_temp:
            min_temp = sum_temp_in_period
            day_min_temp = day
    print(f'максимальная температура равна {round(max_temp/period,1)} была c {day_max_temp+1} по {day_max_temp + period} {mounth}')
    print(f'минимальная температура равна {round(min_temp/period,1)} была с {day_min_temp + 1} по {day_min_temp + period} {mounth}')   

def zadazha3():

    temp_in_may = [random.randint(12, 23) for _ in range(31)]
    temp_in_june =[random.randint(16,28) for _ in range(30)]
    temp_in_july =[random.randint(19,32) for _ in range(31)]
    temp_in_august =[random.randint(20,28) for _ in range(30)]
    temp_in_september =[random.randint(15,24) for _ in range(31)]
    period = 7
    all_mounth = 5
    new_array = [0] * all_mounth

    for i in range(all_mounth):
        if i == 0:
            new_array[i] = temp_in_may
        elif i ==1:
             new_array[i] =temp_in_june
        elif i == 2:
             new_array[i] =temp_in_july    
        elif i == 3:
            new_array[i] =temp_in_august
        else:
             new_array[i] =temp_in_september 

    for row in new_array:
        print(row) 

    # print(f'все температуры {temp_in_may}')
    period_for_mounth(temp_in_may,period, 'мая')
    # print(f'все температуры {temp_in_june}')
    period_for_mounth(temp_in_june,period, 'июня')
    # print(f'все температуры {temp_in_july}')
    period_for_mounth(temp_in_july, period, 'июля')
    # print(f'все температуры {temp_in_august}')
    period_for_mounth(temp_in_august, period, 'августа')
    # print(f'все температуры {temp_in_september}')
    period_for_mounth(temp_in_september, period, 'сентября')
   

zadazha3()
# zadacha2()
# zadacha1()