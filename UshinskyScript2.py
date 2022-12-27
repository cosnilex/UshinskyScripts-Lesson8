#!/usr/bin/python3

class Human:
    """Класс людей, их признаки и поведение"""
    def __init__(self, First_name, Last_name, gender,
                 age, weight, Nationality, school):
        """Стандартные признаки людей

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            Имя, фамилия, пол, возраст, вес, национальность, школа
        """

        self.First_name = First_name
        self.Last_name = Last_name
        self.gender = gender
        self.age = age
        self.weight = weight
        self.Nationality = Nationality
        self.school = school

    def info_humans(self):
        """Информация о человеке

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            Полную информацию по человеку
        """

        print(f'{self.First_name}, {self.Last_name}, {self.gender}, '
              f'{self.age}, {self.weight}, {self.Nationality}, '
              f'{self.school},')

    def say_something(self, text):
        """Метод речи

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            Имя человека и то, что он сказал
        """
        print(f'{self.First_name} сказал(а): {text} ')

    def thinking(self, some):
        """Метод размышления

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            Имя человека и то, о чём он думает
        """
        print(f'{self.First_name} думает о: {some}')

    def buy(self, purchase):
        """Метод покупки

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            Имя человека и то, что он купил
        """
        print(f'{self.First_name} купил(а): {purchase}')


class Student(Human):
    """Класс студентов, наследует Human"""
    def __init__(self, First_name, Last_name,
                 gender, age, weight, Nationality,
                 school, number_of_homeworks):
        """Стандартные признаки студентов

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            Все признаки класса "Human"
            +
            Количество сданных дз (number_of_homeworks)
        """

        super().__init__(First_name, Last_name, gender, age,
                         weight, Nationality, school)

        self.number_of_homeworks = number_of_homeworks

    def homeworks(self):
        """Метод показателя сданных работ у студентов

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            Имя, фамилию студента и количество сданных им домашних работ
        """
        if self.gender == 'male':
            print(f'{self.First_name} {self.Last_name} '
                  f'сдал {self.number_of_homeworks} ДЗ')
        else:
            print(f'{self.First_name} {self.Last_name} '
                  f'сдала {self.number_of_homeworks} ДЗ')

    def compare(self, other):
        """Метод сравнения количества сданных дз у студентов

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
            other - объект с которым нужно произвести сравнение (другой студент)
        Возвращает:
            True или False по каждому сранению
            (равенство дз, меньше дз, больше дз)
        """
        eq = self.number_of_homeworks.__eq__(other.number_of_homeworks)
        less = self.number_of_homeworks.__lt__(other.number_of_homeworks)
        more = self.number_of_homeworks.__gt__(other.number_of_homeworks)

        return print(f'Сравнение {self.First_name}({self.number_of_homeworks}) с '
                     f'{other.First_name}({other.number_of_homeworks})\n'

                     f'Равное количество сданных дз? {eq} '
                     f'\n{self.First_name} сдал(а) меньше дз чем {other.First_name}? {less} '
                     f'\n{self.First_name} сдал(а) больше дз чем {other.First_name}? {more}')


# Создаём экземпляры класса:

try:
    Vasya = Student('Вася', 'Пупкин', 'male', 20, 68, 'russian', '№22', 8)
    Petya = Student('Петя', 'Кузнецов', 'male', 21, 70, 'russian', '№22', 10)
    Tanya = Student('Таня', 'Терешкова', 'female', 20, 58, 'russian', '№22', 9)

except TypeError:
    print('Недостаточное количество аргументов')

# Вызываем методы у экземпляров класса:

try:
    Vasya.homeworks()
    Petya.homeworks()
    Tanya.homeworks()
    print(f'')
    Vasya.compare(Tanya)
    print(f'')
    Petya.compare(Vasya)
    print(f'')
    Tanya.compare(Petya)

except AttributeError:
    print('Несуществующий аттрибут')
