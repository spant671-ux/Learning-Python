temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled.")
else:
    print("The outdoor event is still scheduled.")

temp2 = 30
is_sunny = True

if temp2 >= 28 and is_sunny:
    print("It is hot outside 🥵")
    print("It is SUNNY 🔆")
elif temp2 <= 0 and is_sunny:
    print("It is cold outside 🥶")
    print("It is SUNNY 🔆")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside 😊")
    print("It is SUNNY 🔆")
    