if_auto = False
user_name = ''
user_email = ''
searching = ''
result = ''

user_id = 0

titles = ["тест 'какая/ой ты собака?'", "тест 'какой/ая ты напиток?'", "тест 'какая/ой ты кошка/кот?'",
          "тест 'какая/ой ты шиншилла?'"]

dog = {
    'бульдог': ['Сангвинник', 'Ассам', 'Кино', 'Силы', 'Желтый'],
    'пудель': ['Флегматик', 'Улун', 'Рисование', 'Богатство', 'Синий'],
    'гончая': ['Холерик', 'Фруктовый', 'Спорт', 'Бессмертие', 'Красный'],
    'бобтейл': ['Меланхолик', 'Нет', 'Книги', 'Любовь', 'Зеленый']
}

dog_inv = {
    '1': ['Сангвинник', 'Флегматик', 'Холерик', 'Меланхолик'],
    '2': ['Улун', 'Ассам', 'Фруктовый', 'Нет'],
    '3': ['Кино', 'Рисование', 'Спорт', 'Книги'],
    '4': ['Силы', 'Богатство', 'Любовь', 'Бессмертие'],
    '5': ['Желтый', 'Синий', 'Красный', 'Зеленый']
}

dog_results = {
    'бульдог': 0,
    'пудель': 0,
    'гончая': 0,
    'бобтейл': 0
}

drink = {
    'кофе': ['Волнение', 'Дождь', 'Осень', 'Детектив', 'Заранее'],
    'сок': ['Жизнерадостный', 'Солнце', 'Лето', 'Роман', 'Ничего'],
    'молочный коктейль': ['Мечтательный', 'Снег', 'Зима', 'Фэнтези', 'Умею'],
    'чай': ['Задумчивый', 'Облачно', 'Весна', 'Фантастика', 'Прокрастинирую']
}

drink_inv = {
    '1': ['Волнение', 'Жизнерадостный', 'Мечтательный', 'Задумчивый'],
    '2': ['Дождь', 'Солнце', 'Снег', 'Облачно'],
    '3': ['Осень', 'Лето', 'Зима', 'Весна'],
    '4': ['Детектив', 'Фантастика', 'Роман', 'Фэнтези'],
    '5': ['Заранее', 'Ничего', 'Умею', 'Прокрастинирую']
}

drink_results = {
    'кофе': 0,
    'сок': 0,
    'молочный коктейль': 0,
    'чай': 0
}

cat = {
    'мейн-кун': ['Искусство', 'Экстраверт', 'Инди', 'Инстаграм', 'Да'],
    'сиамская кошка': ['Математика', 'Амбиверт', 'Рок', 'Фейсбук', 'Иногда'],
    'русская голубая': ['Гуманитарные науки', 'Незнаю', 'Поп', 'ВК', 'Неиспытывал'],
    'сфинкс': ['Биология', 'Интроверт', 'Рэп', 'Твиттер', 'Нет']
}

cat_inv = {
    '1': ['Математика', 'Гуманитарные науки', 'Биология', 'Искусство'],
    '2': ['Амбиверт', 'Экстраверт', 'Интроверт', 'Незнаю'],
    '3': ['Рок', 'Рэп', 'Поп', 'Инди'],
    '4': ['Фейсбук', 'Твиттер', 'Инстаграм', 'ВК'],
    '5': ['Нет', 'Да', 'Иногда', 'Неиспытывал']
}

cat_results = {
    'мейн-кун': 0,
    'сиамская кошка': 0,
    'русская голубая': 0,
    'сфинкс': 0
}

chin = {
    'малая длиннохвостая шиншилла': ['Комедия', 'Семья', 'Высота', 'Трудолюбие', 'Да'],
    'береговая шиншилла': ['Артхаус', 'Группа', 'Одиночество', 'Ум', 'Нетда'],
    'короткохвостая шиншилла': ['Боевик', 'Друг', 'Разочарованность', 'Чувственность', 'Данет'],
    'большая шиншилла': ['Фантастика', 'Один', 'Смерть', 'Харизма', 'Нет']
}

chin_inv = {
    '1': ['Комедия', 'Боевик', 'Фантастика', 'Артхаус'],
    '2': ['Группа', 'Семья', 'Друг', 'Один'],
    '3': ['Одиночество', 'Смерть', 'Высота', 'Разочарованность'],
    '4': ['Ум', 'Харизма', 'Трудолюбие', 'Чувственность'],
    '5': ['Данет', 'Нетда', 'Да', 'Нет']
}

chin_results = {
    'малая длиннохвостая шиншилла': 0,
    'береговая шиншилла': 0,
    'короткохвостая шиншилла': 0,
    'большая шиншилла': 0
}



last_dog = ''
dog_ins = [0, 0, 0, 0, 0]
dog_spisok = []

last_temp = ''
last_temp_num = ''

last_tea = ''
last_tea_num = ''

last_hobbie = ''
last_hobbie_num = ''

last_power = ''
last_power_num = ''

last_man = ''
last_man_num = ''

last_drink = ''
drink_ins = [0, 0, 0, 0, 0]
drink_spisok = []

last_char = ''
last_char_num = ''

last_wea = ''
last_wea_num = ''

last_time = ''
last_time_num = ''

last_genre = ''
last_genre_num = ''

last_color = ''
last_color_num = ''

last_cat = ''
cat_ins = [0, 0, 0, 0, 0]
cat_spisok = []

last_sub = ''
last_sub_num = ''

last_type = ''
last_type_num = ''

last_mus = ''
last_mus_num = ''

last_app = ''
last_app_num = ''

last_fri = ''
last_fri_num = ''


last_chin = ''
chin_ins = [0, 0, 0, 0, 0]
chin_spisok = []

last_film = ''
last_film_num = ''

last_people = ''
last_people_num = ''

last_fear = ''
last_fear_num = ''

last_like = ''
last_like_num = ''

last_believe = ''
last_believe_num = ''
