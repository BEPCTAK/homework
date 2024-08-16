#     Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# сразу вычислим средний балл grades сложив сумму оценок и разделив на их количество (sum(grades[])) / (len(grades[]))
grades1 = (sum(grades[0])) / (len(grades[0])), (sum(grades[1])) / (len(grades[1])), (sum(grades[2])) / (len(grades[2])),(sum(grades[3])) / (len(grades[3])),(sum(grades[4])) / (len(grades[4]))
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# делаем список students1 в алфавитном порядке
students1 = list(students)
students1.sort()
HF = dict(zip(students1, grades1))
print(HF)
# автоматика))
print("Введите имя ученика:")
name = input( )
print('Cредний балл', (HF[name]))