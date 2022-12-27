#!/usr/bin/python3

from datetime import datetime
import time
import logging


def runtime(func):
    """Декоратор времени выполнения функции

    Принимает:
        func - нашу функцию у которой нужно узнать время её выполнения

    Возвращает:
        Время выполнения этой функции
    """

    def wrapper(a, b):
        start = datetime.now()
        func(a, b)
        end = datetime.now()
        runtime = (end - start).total_seconds() * 1000
        print(f'Вызвана функция {func.__name__}.'
              f'Время выполнения (ms): {runtime}')
    return wrapper


def delay(func):
    """Декоратор задержки выполнения кода (функции)

    Принимает:
        func - нашу функцию, выполнение которой нужно замедлить

    Возвращает:
        Время выполнения кода (функции) с задержкой
    """

    def wrapper(a, b, delay=0):
        start = datetime.now()
        time.sleep(delay)
        func(a, b, delay)
        end = datetime.now()
        delay_runtime = (end - start).total_seconds() * 1000
        print(f'Вызвана функция {func.__name__}. '
              f'Время выполнения (ms): {delay_runtime}')
    return wrapper


def log(func):
    """Декоратор логирования выполнения функции

    Принимает:
        func - нашу функцию, результат которой нужно прологировать в файл

    Возвращает:
        Сообщение в лог файле (в определённом формате),
        о вызове функции и её результате
    """

    def wrap_log(a, b):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        # Создаём или открываем лог файл по имени функции:
        x = logging.FileHandler(f'{name}.log')
        # Задаём определенный формат записи в лог файле:
        y = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(y)
        x.setFormatter(formatter)
        logger.addHandler(x)
        # Задаём формат сообщения в лог файле о нашей функции:
        logger.info(f'Вызов функции: {name}')
        result = func(a, b)
        logger.info(f'Результат: {result}')
        return func
    return wrap_log


# Добавляем декораторы к нашей функции
# прологируем вызов и результат функции (в файл)
# и узнаем время её выполнения (в консоле):

@runtime
@log
def sum_to_log_file(a, b):
    print(f'сложить: {a} и {b}')
    return a + b


# Теперь замедлим выполнение функции
# добавим произвольную задержку (delay) при вызове функции
# и узнаем время выполнения кода с задержкой (в консоле):

@delay
def delay_s(a, b, delay=0):
    print(f'сложить: {a} и {b}, задержка (ms): {delay}')
    return a + b

# Вызываем функции с заданными аргументами
# у "delay_s" в качестве третьего аргумента
# добавляем задержку:


try:
    sum_to_log_file(2, 4)
    delay_s(2, 6, 2)
except TypeError:
    print('Пропущены аргумент(ы) при вызове функции')
