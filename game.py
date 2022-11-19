import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    min = 1 
    max = 101
        
     
    while True: 
        count+=1 
        mid = round((min+max) / 2)
        if mid > number:
            max = mid
        elif mid < number:
            min = mid
        else:
            print(mid)
            break #конец игры выход из цикла
    return count 

print(f'Количество попыток: {random_predict(55)}')

