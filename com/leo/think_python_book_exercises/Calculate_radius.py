import math


def calculate_r(r):
    return (4 / 3) * math.pi * math.pow(r, 3)


def calculate_total_cost_for_books(books):
    return 3 + 0.75 * (books - 1) + (24.95 * 0.4 * books)


# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
# tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
def calculate_time_until_I_get_home(starting_time):
    time = 45  # 4.5
    f, decpart = math.modf(starting_time)  # 0.55
    if time + time + (f * 100 + 0.000000000000001) >= 60:
        spasticvalue = (((time + (f * 100 + 0.000000000000001)) - 60) * 0.1)
        fu, nodec = math.modf(float(starting_time + 1))
        return float(nodec + float(spasticvalue * 0.1))
    else:
        return float(starting_time + time * 0.10)


print(calculate_r(5))
print(calculate_total_cost_for_books(60))
print(calculate_time_until_I_get_home(7.05))
