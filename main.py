import pprint


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


def geo_filter(geo_list):
    filtered_geo_logs = []
    for x in geo_list:
        if  'Россия' in list(x.values())[0]:
            filtered_geo_logs.append(x)
    return filtered_geo_logs

# print(geo_filter(geo_logs))

# Выведите на экран все уникальные гео-ID из значений словаря ids.

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


def geo_id(geo_is_dict):
    lst = ids.values()
    newlist = []
    for x in lst:
        for y in x:
            newlist.append(y)
    return(set(newlist))

# print(geo_id(ids))
# Дан список поисковых запросов. Получить распределение количества слов в них. Т.е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'Пионер идёт домой сегодня'
    ]


def foo(item):
    storage = {}
    final = {}
    for query in queries:
        words = query.split()

        if len(words) in storage.keys():
            storage[len(words)] += 1
        else:
            storage.update({
                len(words): 1
            })

    for key, value in storage.items():
        percentage = round((value / len(queries)) * 100, 2)
        final.update({
            key : (value, percentage)
        })
    return final

# print(foo(queries))


# Дана статистика рекламных каналов по объемам продаж.
# Напишите скрипт, который возвращает название канала с максимальным объемом.
# Т.е. в данном примере скрипт должен возвращать 'yandex'.

stats = {'facebook': 6512, 'yandex': 123, 'vk': 115, 'google': 99, 'email': 742, 'ok': 98}

max_val = max(stats, key=stats.get)

# print(max_val)