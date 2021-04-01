months = [2200, 2350, 2600, 2130, 2190]
# money expenses jan compered to feb
dif = months[1] - months[0]
if dif > 0:
    print('On february we spent ', dif, ' more euros')
elif dif < 0:
    print('On february we spent ', abs(dif), ' less euros')
else:
    print('We spent the same amount')
print('Total expenses are ', months[0] + months[1] + months[2])

for i in months:
    if i == 2000:
        print('On month ', (i + 1), 'you spent 2000')
        break
months.append(1980)
print(months)
print(months[3])
months[3] = months[3] + 200
print(months[3])