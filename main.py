print('-------------Task1-------------------\n')
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
def geo_logs_russia():
    t = []
    for visit in geo_logs:
        for key, value in dict(visit).items():
            if value[1] == 'Россия':
                del visit[key]
                visit[key] = value
                # print(visit)
                t.append(visit)
    return t

print('-------------Task2-------------------\n')
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def unic_id():
    ids_unic = []
    for key, value in dict(ids).items():
        for values in value:
            if values not in ids_unic:
                ids_unic.append(values)
    print(ids_unic)
    return ids_unic
unic_id()
print('-------------Task3-------------------\n')

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]
def queries_percent():
    queries_perc = []
    word = 'слов'
    for i in queries:
        queries_perc.append(len(i.split()))
    for i in set(queries_perc):
        j = queries_perc.count(i)
        if j == 1:
            d = 'а'
            # print(f'Поисковых запросов из {i} {word + d} - {round(j / len(queries) * 100, 2)}%')
            return f'Поисковых запросов из {i} {word + d} - {round(j / len(queries) * 100, 2)}%'
        else:
            d = ''
            # print(f'Поисковых запросов из {i} {word + d} - {round(j / len(queries) * 100, 2)}%')
            return f'Поисковых запросов из {i} {word + d} - {round(j / len(queries) * 100, 2)}%'

queries_percent()


print('-------------Task4-------------------\n')
def stats_max():
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    max_value = max(stats.values())
    max_stats = {i: j for i, j in stats.items() if j == max_value}
    return max_stats
    # print(max_stats)

print('-------------Task5-------------------\n')
list = ['2018-01-01', 'yandex', 'cpc', 100]
d = list[-1]
for i in list[-2::-1]:
    d = {i: d}
# print(d)

stats_max()

# if __name__ == '__main__':
#     print_hi('PyCharm')
