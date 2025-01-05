# Удаление дубликатов, замена на _
def search():
    count = int(input())
    amount = input().split()
    result = []
    for i in amount:
        if i not in result:
            result.append(i)
    while len(result) != count:
        result.append('_')
    print(' '.join(result))


search()


# Определение индекса для вставки
def search_s():
    amount = [int(i) for i in input().split()]
    count = int(input())
    if count in amount:
        index = amount.index(count)
    else:
        amount.append(count)
        # ints = [int(x) for x in amount]
        amount = sorted(amount)
        index = amount.index(count)
    return print(index)


if __name__ == '__main__':
    # amount = '1 5 10 11'
    # count = 2
    search_s()


def fib_generation(n: int) -> int:
    """
    Фибоначчи.
    """
    if n == 0 or n == 1:
        return 1
    return fib_generation(n - 1) + fib_generation(n - 2)


if __name__ == '__main__':
    generation_number = int(input())
    print(fib_generation(generation_number))


# Бинарный поиск
wins = [1223125, 2128437, 2128500, 2741001, 4567687, 4567890, 7495938, 9314543]
my_ticket = 4567890


def find_element(sorted_numbers, element):
    """Находит индекс element в отсортированном списке sorted_numbers."""
    # Левая граница (левый индекс) рассматриваемого набора элементов.
    # В начале работы она равна индексу первого элемента в списке - нулю.
    left = 0
    # Правая граница (правый индекс) рассматриваемого набора элементов.
    # В начале работы она равна индексу последнего элемента в списке.
    right = len(sorted_numbers) - 1
    # Пока левая граница меньше правой или равна ей:
    while left <= right:
        # Находим в наборе элементов индекс среднего элемента.
        mid = (left + right) // 2
        # Если элемент с этим индексом равен искомому, возвращаем его индекс.
        if sorted_numbers[mid] == element:
            return mid
        # Если средний элемент меньше искомого...
        if sorted_numbers[mid] < element:
            # ...то изменяем левую границу поиска:
            left = mid + 1
        # Если средний элемент больше искомого...
        else:
            # ...то изменяем правую границу поиска:
            right = mid - 1
    # Если левая граница оказалась больше правой,
    # значит, элемент не найден. Возвращаем None.
    return None


print(find_element(wins, my_ticket))


# Метод пузырька
example_array = [6, 5, 3, 1, 8, 7, 2, 4]


def bubble_sort(data):
    # Устанавливаем значение last_index равным индексу последнего элемента.
    last_index = len(data) - 1
    # Чтобы цикл while мог стартовать, устанавливаем флаг в значение True.
    swapped = True
    # Цикл будет выполняться, если флаг swapped = True. Это значение
    # устанавливается при первом проходе и в случае, если на предыдущем проходе
    # были перестановки.
    # Если перестановок не было, то цикл перестанет выполняться.
    while swapped:
        # Для текущего прохода сбрасываем значение флага на False.
        swapped = False
        # Внутренний цикл - такой же, как и в предыдущем листинге.
        # Формируем внутренний цикл от 0 до last_index (исключая last_index).
        for item_index in range(last_index):
            # Сравниваем значения элементов списка.
            if data[item_index] > data[item_index + 1]:
                # Если значения надо поменять местами - меняем.
                data[item_index], data[item_index + 1] = (
                    data[item_index + 1], data[item_index]
                )
                # Выставляем флаг "выполнена перестановка".
                swapped = True
        # Уменьшаем значение last_index на единицу.
        last_index -= 1
    # Возвращаем отсортированный список.
    return data


print(bubble_sort(example_array))


# Ищем число
def find_two_indexes(data, expected_result):
    # В начале работы
    # - левый указатель указывает на первый элемент списка (с индексом 0):
    left_pointer = 0
    # - правый указатель указывает на последний элемент;
    # индекс этого элемента на единицу меньше длины списка.
    right_pointer = len(data) - 1
    # Пока индекс левого указателя меньше индекса правого указателя.
    while left_pointer < right_pointer:
        # Считаем сумму двух элементов.
        result = data[left_pointer] + data[right_pointer]
        # Если она совпадает с искомой...
        if result == expected_result:
            # ...возвращаем ответ:
            return left_pointer, right_pointer
        # Если сумма больше искомой, то...
        if result > expected_result:
            # ...надо уменьшить сумму: уменьшаем значение правого указателя.
            right_pointer -= 1
        # Все остальные варианты относятся к случаям,
        # когда сумма меньше искомой.
        else:
            # Сумму надо увеличить,
            # для этого увеличиваем значение левого указателя.
            left_pointer += 1


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_result = 10
    print(find_two_indexes(data, expected_result))


# Наименьшая сумма из срезов.Скользящая строка
def find_min_slice_sum(data, elements_in_slice):
    # Считаем сумму первого окна.
    window_sum = sum(data[0:elements_in_slice])
    # Запоминаем результат подсчёта в качестве минимальной суммы.
    min_sum = window_sum
    # В цикле перебираем индексы массива от elements_in_slice до последнего.
    for index in range(elements_in_slice, len(data)):
        # К сумме предыдущего окна добавляем новый элемент: data[index]
        # и вычитаем "вышедший" элемент: data[index - elements_in_slice]
        window_sum += data[index] - data[index - elements_in_slice]
        # Находим минимальную сумму.
        min_sum = min(min_sum, window_sum)
    return min_sum


if __name__ == '__main__':
    data = [5, -3, -2, 10, 2, 7, 1, -6, 13]
    elements_in_slice = 4
    print(find_min_slice_sum(data, elements_in_slice))


def list_superset(list_set_1, list_set_2):
    # Не меняйте названия функции и параметров. Напишите решение здесь.
    status = 0
    if len(list_set_1) < len(list_set_2):
        for i in list_set_1:
            if i in list_set_2:
                status += 1
        if status == len(list_set_1):
            return f'Набор {list_set_1} - супермножество.'
        else:
            return 'Супермножество не обнаружено.'

    if len(list_set_2) < len(list_set_1):
        for i in list_set_2:
            if i in list_set_1:
                status += 1
        if status == len(list_set_2):
            return f'Набор {list_set_2} - супермножество.'
        else:
            return 'Супермножество не обнаружено.'

    if len(list_set_1) == len(list_set_2):
        for i in list_set_2:
            if i in list_set_1:
                status += 1
        if status == len(list_set_2):
            return 'Наборы равны.'
        else:
            return 'Супермножество не обнаружено.'


# Примеры для проверки функции.
list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))


def longest_unique_substring():
    s = input()  # Пользователь вводит строку
    char_set = set()  # Множество для хранения уникальных символов
    left = 0  # Левый указатель окна
    max_length = 0  # Длина наибольшей подстроки

    for right in range(len(s)):
        while s[right] in char_set:  # Пока символ дублируется
            char_set.remove(s[left])  # Убираем символы из окна
            left += 1  # Сдвигаем левый указатель вправо
        char_set.add(s[right])  # Добавляем текущий символ в множество
        max_length = max(max_length, right - left + 1)

    print(max_length)  # Печатаем результат
    return max_length


longest_unique_substring()
