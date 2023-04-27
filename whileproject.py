import random

shot_count = 0
distance_left = 580

print("Choose your club wisely for this course. It is a par 5 with 580 yards.\n")

while distance_left > 0:
    shot_choice = input(f"You have {distance_left} yards left to the green. What is your club choice: driver, woods, hybrid, iron 3, iron 5, iron 7, 56, or 60?\n")

    if shot_choice == "driver":
        distance = random.randint(270, 320)
        location = random.choice(["fairway", "rough"])
        print(f"You hit your driver {distance} yards into the {location}.\n")
        shot_count += 1

    elif shot_choice == "woods" or shot_choice == "hybrid":
        distance = random.randint(200, 250)
        location = random.choice(["fairway", "rough"])
        print(f"You hit your {shot_choice} {distance} yards down the {location}.\n")
        shot_count += 1

    elif shot_choice == "iron 3" or shot_choice == "3":
        distance = random.randint(180, 210)
        location = random.choice(["fairway", "rough"])
        print(f"You hit your {shot_choice} {distance} yards down the {location}.\n")
        shot_count += 1

    elif shot_choice == "iron 5" or shot_choice == "5":
        distance = random.randint(distance_left-15, distance_left-10)
        print(f"You hit your {shot_choice} {distance} yards and made it onto the green.\n")
        shot_count += 1

    elif shot_choice == "iron 7" or shot_choice == "7":
        distance = random.randint(distance_left-17, distance_left-11)
        print(f"You hit your {shot_choice} {distance} yards and made it onto the green.\n")
        shot_count += 1

    elif shot_choice == "56":
        distance = random.randint(distance_left-15, distance_left-10)
        print(f"You hit your {shot_choice} {distance} yards and made it onto the green.\n")
        shot_count += 1

    elif shot_choice == "60":
        distance = random.randint(distance_left-20, distance_left-10)
        print(f"You hit your {shot_choice} {distance} yards and made it onto the green.\n")
        shot_count += 1

    else:
        print("Invalid club choice. Please choose driver, woods, hybrid, iron 3, iron 5, iron 7, 56, or 60.")
        continue

    if location == "rough":
        distance -= 20
        print("Your ball is in the rough, so your next shot will travel 20 yards less than expected.\n")

    distance_left -= distance

putts = 0
while distance_left < 0:
    put_distance = random.randint(1,9)
    if put_distance > abs(distance_left):
        put_distance = abs(distance_left)
    distance_left += put_distance
    putts += 1

print(f"You made it to the green and it took you {putts} putts to finish the hole.")
score = shot_count + putts
print(f"Your total score for the hole is {score}.")

