def valid_mountain_array():
    amount = [int(i) for i in input().split()]
    status = False
    final = False
    for b in range(len(amount)):
        if amount.count(b) > 2:
            final = False
            break
        if b != (len(amount)-1) and amount[b] < amount[b + 1]:
            status = True
            final = False
        if status is True and b != (len(amount)-1) and amount[b] > amount[b + 1]:
            final = True
        if b != (len(amount)-1) and amount[b] == amount[b + 1]:
            final = False
            break
    return final


print(valid_mountain_array())
