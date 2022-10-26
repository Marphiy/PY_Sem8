"""
Задание 1.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
Пример:
1 2 3
4 5 6
7 8 9
1 2 3
4 5 6
7 8 9
Сумма матриц:
2 4 6
8 10 12
14 16 18
"""
import random

class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        
    def __str__(self):
        return f'{self.list_of_lists}'
    
    def __add__(self, other):
        sum_of_matrs = [[0, 0, 0], 
                       [0, 0, 0], 
                       [0, 0, 0]]
        for i in range(len(self.list_of_lists[0])): 
            for k in range(len(self.list_of_lists[1])): 
                sum_of_matrs[i][k] = self.list_of_lists[i][k] + other.list_of_lists[i][k]
        return f'{sum_of_matrs}'

    def new_matrix(self):
        self.list_of_lists = [[random.randint(0, 10) for e in range(3)] for e in range(3)]
                

m_1 = [[0],[0],[0]]

mat_1 = Matrix(m_1)
mat_2 = Matrix(m_1)
mat_1.new_matrix() 
mat_2.new_matrix()
print(f'Матрица 1:{mat_1}\nМатрица 2:{mat_2}')
print()
print(f'Сумма матриц: {mat_1 + mat_2}')



