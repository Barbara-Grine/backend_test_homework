def sorted_func():
    amount_elements = int(input())
    non_sort_list = [int(i) for i in input().split()]
    sorted_list = []
    count = 0
    while len(sorted_list) < amount_elements:
        if not sorted_list:
            sorted_list.extend(non_sort_list[:non_sort_list.index(0)+1])
            del non_sort_list[:non_sort_list.index(0)+1]
            count += 1

        max_value = max(sorted_list)

        min_value = min(non_sort_list)
        index_min = non_sort_list.index(min_value)

        if max_value > min_value:
            sorted_list.extend(non_sort_list[:index_min+1])
            del non_sort_list[:index_min+1]
        else:
            sorted_list.extend(non_sort_list[:index_min+1])
            del non_sort_list[:index_min+1]
            count += 1
    return print(count)


sorted_func()
