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
    # присваеваем значения соответственно для счетчика, нижнего и верхнего диапазонов угадываемого числа
    count, a, z = 0, 1, 101 
    while True:
        # считаем попытки
        count += 1 
        # "угадываем" нужное число с помощью случайного
        predict_number = np.random.randint(a, z) 
        # если угадали, завершаем цикл
        if number == predict_number: 
            break 
        if number < predict_number: # искомое число меньше предложенного
            z = predict_number # тогда присваевыем верхнему диапазону наше случайное число, смысла загадывать больше него уже нет
        if number > predict_number: # искомое число больше предложенного
            a = predict_number # тогда присваевыем нижнему диапазону наше случайное число, смысла загадывать больше него уже нет
    return (count) # возвращаем количество попыток

    
def score_game(random_predict) -> int:
    """За какое количество попыпоток в среднем угадывает 
    за 1000 подходов наш алгоритм

    Args:
        random_predict (_type_): функция угадывания
    Returns:
        int: среднее количество угадываний
    """
    count_ls = [] # список количества попыток
    np.random.seed(1) # фиксируем значения случайной последовательности
    random_array = np.random.randint(1, 101, size=1000) # присваеваем списку random_array попытки в количестве 1000 штук с помощью функции randint
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


if __name__ == "__main__":
    score_game(random_predict)

