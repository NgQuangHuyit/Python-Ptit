travel_fee = {
    'xe_con': {
        '5': 10000,
        '7': 15000
    },
    'xe_tai': {
        '2': 20000
    },
    'xe_khach': {
        '29': 50000,
        '45': 70000
    }
}

profit_per_day = {}

for i in range(int(input())):
    record = input().lower().split()
    if record[3].lower() == 'out':
        continue
    else:
        if record[4] not in profit_per_day.keys():
            profit_per_day[record[4]] = 0
        profit_per_day[record[4]] += travel_fee[record[1]][record[2]]

for day in profit_per_day:
    print(f"{day}: {profit_per_day[day]}")
