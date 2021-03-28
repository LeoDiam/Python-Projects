def calculate_seconds(minutes,sec):
    return (minutes * 100) + sec
def calculate_miles(miles):
    return miles * 1.61
def average_race_pace(miles,minutes,sec):
    return calculate_miles(miles) / ((calculate_seconds(minutes,sec)) / 100)
# def average_race_pace_display_m_and_s(miles,hours,sec):
#        return miles % ((hours/60)*100 + sec)

print(calculate_seconds(42,42))
print(calculate_miles(10))
print(average_race_pace(10,42,42))
