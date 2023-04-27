#!/usr/bin/env python3
import random

distance_left= 580
shot_count= 0
# start
print("Choose your club wisely for this course. It is a par 5 with 580 yards.\n")

# first shot
shot_choice= ""
while shot_choice not in ["driver","woods","hybrid"]:
    shot_choice = input("What is your first club choice: driver, woods, or hybrid?\n")

if shot_choice  == "driver":
    distance = random.randint(270, 320)
    location = random.choice(["fairway", "rough"])
    print(f"You hit your driver {distance} yards into the {location}.\n")
    shot_count += 1

elif shot_choice in ["woods","hybrid"]:
    distance = random.randint(200, 250)
    location = random.choice(["fairway", "rough"])
    print(f"You hit your {club_choice} {distance} yards down the {location}.\n")
    shot_count += 1

distance_left -= distance

# rough situation
if location == "rough":
    distance -= 20
    print("Your ball is in the rough, so your second shot will travel 20 yards less than expected.\n")

distance_left = 580 - distance
print(f"You have {distance_left} yards left to the green.\n")

# second shot
second_choice = input("Choose your second club: hybrid or iron 3?\n")
if second_choice == "hybrid":
   second_distance = random.randint(210, 230)
   print(f"You hit your {second_choice} {second_distance} yards\n")
   shot_count += 1

elif second_choice == "iron 3" or second_choice == "3":
    second_distance = random.randint(180, 210)
    print(f"You hit your {second_choice} {second_distance} yards\n")
    shot_count += 1

else:
    print("Invalid club choice. Please choose hybrid or iron 3.\n")


distance_left -= second_distance

# third shot
if distance_left > 100:
    print(f"You have {distance_left} yards left to the green.\n")
    third_choice = input("Choose your third club:iron 5 or iron 7\n")
    if third_choice == "iron 5" or third_choice == "5":
        third_distance = random.randint(distance_left-15, distance_left-10)
        distance_left -= third_distance
        print(f"You hitted {third_distance} made it onto the green remaining distance {distance_left}\n")
        shot_count += 1

    elif third_choice == "iron 7" or third_choice == "7":
        third_distance = random.randint(distance_left-17, distance_left-11)
        distance_left -= third_distance
        print(f"You hitted {third_distance} made it onto the green remaining distance {distance_left}\n")
        shot_count += 1

    else:
        print("Invalid club choice. Please choose iron5 or iron7.\n")
               

elif distance_left <= 100 and distance_left > 10:
    print(f"You have {distance_left} yards left to the green.\n")
    another_third_choice= input("Choose your wedge: 56 or 60\n")
    if another_third_choice == "56":
        third_distance = random.randint(distance_left-15,distance_left-10)
        distance_left -= third_distance
        print(f"You hitted {third_distance} made it onto the green remaining distnace {distance_left}\n")
        shot_count += 1

    elif another_third_choice  == "60":
        third_distance = random.randint(distance_left-20,distance_left-10)
        distance_left -= third_distance
        print(f"You hitted {third_distance } made it onto the green remaining distance {distance_left}\n")
        shot_count += 1

    else:
        print("Invalid club choice. Please choose 56 or 60\n")
        
# put

putts = 0
while distance_left > 0:
    put_distance = random.randint(1,9)
    if put_distance > distance_left:
        put_distance = distance_left
    distance_left -= put_distance
    putts += 1
print(f"You made it to the green and it took you {putts} putts to finish the hole.\n")

# score
score = shot_count + putts
print(f"Your total score for the hole is {score}.\n")

