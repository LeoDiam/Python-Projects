def odd_nums_till_max(max):
    odds = []
    for i in range(1, max):
        if i % 2 == 1:
            odds.append(i)
    return odds


print(odd_nums_till_max(int(input('Input a number '))))
