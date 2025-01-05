# ID проверки: 129394721

def delivery(weights: list[int], limit: int) -> int:
    weights = sorted(weights)
    platforms = 0
    min_weight_index = 0
    max_weight_index = len(weights) - 1
    while min_weight_index <= max_weight_index:
        platforms += 1
        if weights[min_weight_index] + weights[max_weight_index] <= limit:
            min_weight_index += 1
        max_weight_index -= 1
    return platforms


if __name__ == '__main__':
    print(delivery(weights=[int(i) for i in input().split()],
                   limit=int(input())))
