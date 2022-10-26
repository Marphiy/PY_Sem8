"""
Задание 2.
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Единственный класс этого проекта — одежда (класс Clothes).
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property
Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57
Два класса: абстрактный и Clothes
"""

from abc import ABC, abstractmethod


class MyAbstractClass(ABC):

    @abstractmethod
    def get_fabric_consumption(self):
        pass


class Clothes(MyAbstractClass):
    def __init__(self, clothes_type, param):
        self.clothes_type = clothes_type
        self.param = param

    def __str__(self):
        if self.clothes_type == 'Пальто':
            return f'{self.clothes_type} {self.param}-го размера'
        else:
            return f'{self.clothes_type}, рост {self.param}'

    def __add__(self, other):
        return self.get_fabric_consumption() + other.get_fabric_consumption()

    def get_fabric_consumption(self):
        f_c = self.param/6.5+0.5 if self.clothes_type == 'Пальто' else 2*self.param+0.3
        return round(f_c, 2)


c_1 = Clothes('Костюм', 3)
c_2 = Clothes('Пальто', 4)
print(f'{c_1}: расход ткани {c_1.get_fabric_consumption()}')
print(f'{c_2}: расход ткани {c_2.get_fabric_consumption()}')
print(f'Общий расход ткани = {c_1 + c_2}')
