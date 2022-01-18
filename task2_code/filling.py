
# Вспомогательные функции для наполнения базы данных

from app import db, Cats

def add(breed, name, age, description, picture):
	cat = Cats(breed = breed, name = name, age = age, description = description, picture = picture)
	db.session.add(cat)
	db.session.commit()
#

def filling():
	add('Абиссинская', 'Перс', 17, 'Очень красивая', 'pic1')
	add('Мист', 'Чарльз', 15, 'Привередлив к еде', 'pic2')
	add('Табби', 'Мириан', 24, 'Кусается', 'pic3')
	add('Бобтейл', 'Оцелот', 3, 'Почему то лысый', 'pic1')
	add('Жесткошерстная', 'Борис', 25, 'Ничего не делает, ленивый', 'pic4')
	add('Керл', 'Карл', 35, 'Не продается, просто смотрите', 'pic5')
	add('Мау', 'Дзедун', 12, 'Игнорирует хозяев', 'pic6')
	add('Каракал', 'Гоша', 21, 'Большой, не продается', 'pic7')
	add('Манул', 'Третий', 23, 'Медленно ходит', 'pic8')
	add('Балинез', 'Сэм', 30, 'Ловит мышей', 'pic9')
	add('Бенгальская', 'Говард', 6, 'Громко ходит', 'pic10')
	add('Бомбейская', 'Сьюзен', 35, 'Забирайте, все прививки сделаны', 'pic11')
	add('Короткошерстная', 'Федор', 34, 'Подходит для охраны дома', 'pic12')
	add('Бурма', 'Алан', 15, 'Крайне полезный кот', 'pic1')
	add('Гавана', 'Грегор', 16, 'Умеет открывать двери', 'pic2')
	add('Девон рекс', 'Чиж', 20, 'Много гуляет', 'pic3')
	add('Домашняя', 'Жучка', 31, 'Всегда найдет путь к дому', 'pic4')
	add('Донской сфинкс', 'Илья', 26, 'Почему то мохнатый', 'pic5')
	add('Кельтская', 'Локк', 30, 'Слишком энергичный', 'pic6')
	add('Йорк', 'Джимми', 33, 'Ворует еду', 'pic7')
	add('Калифорнийская сияющая', 'Джесси', 22, 'Быстро бегает', 'pic8')
	add('Канаани', 'Говард', 14, 'Появляется в самых неожиданных местах', 'pic9')
	add('Кимрик', 'Торвальд', 13, 'От него не спрячешься', 'pic10')
	add('Корат', 'Нильсон', 40, 'Не уживается с собаками', 'pic11')
	add('Корниш рекс', 'Дымок', 24, 'Собирает пыль', 'pic12')
	add('Лаперм', 'Кесса', 42, 'Глаза ярко светятся в ночи', 'pic1')
	add('Лаперм', 'Тишка', 25, 'Все сбросит со стола', 'pic2')
	add('Манчкин', 'Тимка', 5, 'С рождения умеет плавать', 'pic3')
	add('Манул', 'Люси', 12, 'Не стоит трогать', 'pic4')
	add('Мейн-кун', 'Бон', 17, 'Большой, мохнатый, опасный', 'pic5')
	add('Меконгский бобтейл', 'Маус', 9, 'Выжил после падения с девятиэтажки', 'pic6')
	add('Нибелунг', 'Ганс', 32, 'Слишком высокомерный взгляд', 'pic7')
#
