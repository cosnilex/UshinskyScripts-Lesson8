#!/usr/bin/python3

class animals:
    """Класс животных, их признаки и поведение"""
    def __init__(self, Generic_name, gender, age,
                 colour, weight, type_of_food):
        """Стандартные признаки животных

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
            Generic_name - название животного (зебра, слон, черепаха)
            gender - пол животного
            age - возраст
            colour - цвет
            weight - вес
            type_of_food - травоядное, хищник, всеядное
        """

        self.Generic_name = Generic_name
        self.gender = gender
        self.age = age
        self.colour = colour
        self.weight = weight
        self.type_of_food = type_of_food

    def info(self):
        """Информация по животному

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            Полную информацию по животному
        """
        print(f'{self.Generic_name}, {self.gender}, '
              f'{self.age}, {self.colour}, '
              f'{self.weight}, {self.type_of_food}')

    def move(self):
        """Метод перемещения животного

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            Сообщение о том, что животное перемещается
        """
        print(f'{self.Generic_name} перемещается')

    def reproduction(self):
        """Метод продолжения рода

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            Сообщение о том, что животное продолжает род
        """
        print(f'{self.Generic_name} продолжает род')

    def breath(self):
        """Метод дыхания

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            Сообщение о том, что животное дышит
        """
        print(f'{self.Generic_name} дышит')

    def aging(self):
        """Метод старения

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            Сообщение о том, что животное постарело на один год
        """
        self.age += 1
        print(f'{self.Generic_name} постарел(а) на один год, '
              f'теперь ему(ей) {self.age} лет/год(а)')

    def eating(self):
        """Метод питания

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            Сообщение о том, что животное ест пищу и тип потребления пищи
        """
        print(f'{self.Generic_name} ест пищу, он(а) {self.type_of_food}')


class mammals(animals):
    """Класс млекопитающих, их признаки и поведение"""
    def __init__(self, Generic_name, gender, age,
                 colour, weight, type_of_food,
                 coat_hair_colour):
        """Стандартные признаки млекопитающих

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            Все признаки класса "animals"
            +
            coat_hair_colour - цвет шерсти/волос
        """

        super().__init__(Generic_name, gender, age, colour,
                         weight, type_of_food)

        self.coat_hair_colour = coat_hair_colour

    def info_mammals(self):
        """Информация по млекопитающемуся

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            Полную информацию по млекопитающемуся
        """
        print(f'{self.Generic_name}, {self.gender}, {self.age}, '
              f'{self.weight}, {self.type_of_food}, {self.coat_hair_colour}')

    def milk(self):
        """Метод вскармливания молоком

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            Если экземляр класса самка - сообщение о том,
            что она вскармливает своё потомство молоком
            Если экземляр класса самец - сообщение о том,
            что мужской род не может вскармиливать потомство молоком
        """
        if self.gender == 'female':
            print(f'{self.Generic_name} вскармливает потомство молоком')
        else:
            print(f'{self.Generic_name} '
                  f'мужской род не может вскармливать потомство молоком')


class Human(mammals):
    """Класс людей, их признаки и поведение"""
    def __init__(self, Generic_name, First_name, Last_name,
                 gender, age, colour, weight,
                 Nationality, type_of_food, coat_hair_colour, work,
                 school, income):
        """Стандартные признаки людей

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            Все признаки класса "mammals"
            +
            Имя, фамилия, национальность, работа, школа, зарплата(доход)
        """

        super().__init__(Generic_name, gender, age, colour,
                         weight, type_of_food, coat_hair_colour)

        self.First_name = First_name
        self.Last_name = Last_name
        self.Nationality = Nationality
        self.work = work
        self.school = school
        self.income = income

    def info_humans(self):
        """Информация по людям

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            Полную информацию по человеку
        """

        print(f'{self.Generic_name}, {self.First_name}, '
              f'{self.Last_name}, {self.gender}, '
              f'{self.age}, {self.colour}, '
              f'{self.Nationality} {self.weight}, '
              f'{self.coat_hair_colour}, {self.work}, '
              f'{self.school}, {self.income}')

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


class cat(mammals):
    """Класс котов, их признаки и поведение"""
    def __init__(self, Generic_name, Name, gender,
                 age, colour, weight, type_of_food,
                 coat_hair_colour, colour_of_tail):
        """Стандартные признаки котов

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            Все признаки класса "mammals"
            +
            цвет хвоста
        """

        super().__init__(Generic_name, gender, age, colour,
                         weight, type_of_food, coat_hair_colour)
        self.colour_of_tail = colour_of_tail
        self.Name = Name

    def info_cats(self):
        """Информация по котам

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            Полную информацию по коту(кошке)
        """
        print(f'{self.Generic_name}, {self.Name}, {self.gender}, '
              f'{self.age}, {self.weight}, {self.coat_hair_colour}, '
              f'{self.colour_of_tail},')

    def meow(self):
        """Метод мяуканья

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            название животного + имя кота + сообщение о том, что он мяукнул
        """
        print(f'{self.Generic_name} {self.Name}: мяукнул(а)')

    def wash(self):
        """Метод умывания

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            название животного + имя кота + сообщение о том, что он умывается
        """
        print(f'{self.Generic_name} {self.Name}: умывается языком')


class dog(mammals):
    """Класс собак, их признаки и поведение"""
    def __init__(self, Generic_name, Name, gender,
                 age, breed, colour, weight,
                 type_of_food, coat_hair_colour,
                 colour_of_tail, commands_knowledge):
        """Стандартные признаки собак

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            Все признаки класса "mammals"
            +
            порода, цвет хвоста, знание комманд
        """

        super().__init__(Generic_name, gender, age, colour,
                         weight, type_of_food, coat_hair_colour)
        self.colour_of_tail = colour_of_tail
        self.Name = Name
        self.breed = breed
        self.commands_knowledge = commands_knowledge

    def info_dogs(self):
        """Информация по собакам

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            Полную информацию по собаке
        """
        print(f'{self.Generic_name}, {self.Name}, {self.gender}, '
              f'{self.age}, {self.breed}, {self.weight}, '
              f'{self.coat_hair_colour}, {self.colour_of_tail}, '
              f'{self.commands_knowledge}')

    def bark(self):
        """Метод гавканья

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
             название животного + имя собаки +
             сообщение о том, что собака гавкнула
        """
        print(f'{self.Generic_name} {self.Name}: гавкнул(а)')

    def wag_tail(self):
        """Метод виляния хвостом

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            название животного + имя собаки +
            сообщение о том, что собака виляет хвостом
        """
        print(f'{self.Generic_name} {self.Name}: виляет хвостом')

    def command(self):
        """Метод исполнения команд хозяина

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
        Возвращает:
            в случае, если собака умеет исполнять команды, выводится имя собаки
            и сообщение о том, что команда исполнена.
            Если не умеет, имя собаки + не умеет исполнять команды.
        """
        if self.commands_knowledge == 'yes':
            print(f'{self.Name}: исполнил команду хозяина')
        else:
            print(f'{self.Name}: не умеет исполнять команды')


# Создаём экземпляры под каждый из наших классов


try:
    Crocodile = animals('Крокодил', 'male', 60, 'green', 210, 'хищник')

    Fox = mammals('Лиса', 'female', 1, 'orange', 7, 'хищник', 'orange')

    Alex = Human('Человек', 'Alex', 'Orlov', 'male',
                 27, 'white', 70, 'russian',
                 'всеядный', 'dark', 'писатель',
                 '№ 71, Ярославль', 70000)

    Matroskin = cat('Кот', 'Матроскин', 'male', 7,
                    'white-grey', 4, 'хищник',
                    'white-grey', 'striped-white-grey')

    Bobik = dog('Собака', 'Бобик', 'male', 10,
                'такса', 'brown', 8, 'всеядный',
                'brown', 'white-brown', 'yes')

except TypeError:
    print('Недостаточное количество аргументов')


# Начинаем вызывать различные методы у разных экземпляров класса:


try:
    print(Crocodile.age)
    Crocodile.breath()
    print(Fox.colour)
    Fox.reproduction()
    print(Alex.Nationality)
    Alex.buy('Машина')
    print(Matroskin.weight)
    Matroskin.info_cats()
    print(Bobik.commands_knowledge)
    Bobik.command()
except AttributeError:
    print('Несуществующий аттрибут')
