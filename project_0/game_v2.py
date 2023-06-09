"""Игра угадай число
Компьютер сам загадывает и сам угадывает
"""

import numpy as np 


def random_predict(number:int = 1) -> int:
    """ Рандомно угадываем число

    Args:
       number (int, optional): Загаданное число. Defaults to 1.
    Returns:
       int: Число попыток
    """    
    # Инициализация счетчика и границ интервала для генерации случайных чисел
    count, a, z = 0, 1, 101 
    # Бесконечный цикл, пока не угадаем число
    while True:
        # Считаем попытки, увеличиваем счетчик на 1
        count += 1 
        # Генерируем случайное число в интервале от a до z
        predict_number = np.random.randint(a, z) 
        # Если угадали, прерываем цикл
        if number == predict_number: 
            break 
        # Если загаданное число меньше, то уменьшаем правую границу интервала
        if number < predict_number: 
            z = predict_number
        # Если загаданное число больше, то увеличиваем левую границу интервала    
        if number > predict_number: 
            a = predict_number
    # Возвращаем количество попыток, которое потребовалось для угадывания числа        
    return (count) 

    
def score_game(random_predict) -> int:
    """За какое количество попыпоток в среднем угадывает 
    за 1000 подходов наш алгоритм

    Args:
        random_predict (_type_): функция угадывания
    Returns:
        int: среднее количество угадываний
    """
    # Создаем пустой для сохранения количества попыток угадывания числа
    count_ls = [] 
    # Фиксируем значения случайной последовательности, чтобы результат был воспроизводим
    np.random.seed(1) 
    # Присваеваем списку random_array попытки в количестве 1000 штук с помощью функции randint
    random_array = np.random.randint(1, 101, size=1000) 
    # Проходим циклом по массиву с загаданными числами и вызываем функцию random_predict для каждого из них,
    # сохраняя результаты в список count_ls
    for number in random_array:
        count_ls.append(random_predict(number))
    # Вычисляем среднее значение количества попыток в списке count_ls
    score = int(np.mean(count_ls))
    # Выводим на экран сообщение с результатом
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    # Возвращаем значение среднего количества попыток
    return(score)

# Основная функция, которая запускается при запуске скрипта как основного модуля программы
if __name__ == "__main__":
    # Вызываем функцию score_game для вычисления среднего числа попыток угадывания числа
    score_game(random_predict)

