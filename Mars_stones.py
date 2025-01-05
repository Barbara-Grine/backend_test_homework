def sort_weights(n, orders, m, results):
    orders.sort()
    results.sort()

    i, j = 0, 0
    customer = 0

    while i < n and j < m:
        if results[j] >= orders[i]:
            customer += 1
            i += 1
            j += 1
        else:
            j += 1

    return customer


# def sort_weights_recursive(orders, results, customer=0):
    # Базовый случай: если один из списков пуст
    # if not orders or not results:
    # return customer

    # Сортируем списки на первом шаге
    # orders.sort()
    # results.sort()

    # Рекурсивные проверки
    # if results[0] >= orders[0]:  # Если образец удовлетворяет заказ
    # return sort_weights_recursive(orders[1:], results[1:], customer + 1)
    # else:  # Если образец слишком лёгкий
    # return sort_weights_recursive(orders, results[1:], customer)


if __name__ == "__main__":
    n = int(input())  # Количество заказов
    orders = list(map(int, input().split()))  # Минимальный вес заказов
    m = int(input())  # Количество образцов
    results = list(map(int, input().split()))  # Вес доставленных образцов

    print(sort_weights(n, orders, m, results))
