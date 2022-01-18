
# Решение задания 1

def main():
    print('Введите исходные данные в виде целых чисел')
    red = input('Количество красных машин >')
    white = input('Количество белых машин >')

    try:
        red = int(red)
        white = int(white)
    except ValueError:
        print('Не удалось распознать входные значения')
        print('Программа работает только с целыми положительными числами')
        return

    if red < 0 or white < 0:
        print('На вход получено отрицательное число')
        print('Программа работает только с положительными числами')
        return

    if red == 0 and white == 0:
        print('Решение:')
        print('(пустая строка)')# Этот случай не противоречит формулировке задачи
        return

    if (red > 2 * white) or (white > 2 * red):
        print('Нет решения')
        return

    answer = ''

    if red > white:
        dif = red - white
        answer += 'RWR' * dif
        answer += 'RW' * (white - dif)
    else:
        dif = white - red
        answer += 'WRW' * dif
        answer += 'WR' * (red - dif)

    print('Решение:', answer)
#

if __name__ == '__main__':
    main()
    print('Выполнение программы завершено')
#
