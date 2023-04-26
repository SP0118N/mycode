tiger_woods = {
    'name': 'Tiger Woods',
    'age': 46,
    'profession': 'Professional Golfer',
    'achievements': ['15 major championships', '82 PGA Tour wins',
                     '11-time PGA Tour Player of the Year',
                     '2-time FedEx Cup Champion'],
    }

tiger_woods.update({"club": "Taylormade"})

print(tiger_woods.keys())

choice = input("choose name,age,profession,achievements or club\n")

if choice in tiger_woods:
    print(f"The value for {choice} is {tiger_woods[choice]}")
else:
    wrong= tiger_woods.get(choice, "Invalid Input")
    print(f"wrong input of {wrong}")
