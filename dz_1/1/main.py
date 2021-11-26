duration = int(input('duration = '))

if duration >= 0 and duration < 60:
    print(f'{duration} сек')
elif duration >= 0 and duration < 3600:
    time_min = duration // 60
    time_sec = duration % 60
    print(f'{time_min} мин {time_sec} сек')
elif duration >= 0 and duration < 86400:
    time_hour = duration // 3600
    time_min = (duration % 3600) // 60
    time_sec = (duration % 3600) % 60
    print(f'{time_hour} час {time_min} мин {time_sec} сек')
elif duration >= 0 and duration >= 86400:
    q_day = duration // 86400
    difference = duration - q_day * 86400
    time_hour = difference // 3600
    time_min = (difference % 3600) // 60
    time_sec = (difference % 3600) % 60
    print(f'{q_day} дн {time_hour} час {time_min} мин {time_sec} сек')
else:
    print('Неверные данные')