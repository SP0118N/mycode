#! /usr/bin/env python3
import random

wordbank= ["indentation", "spaces"] 
tlgstudents= ["Brandon", "Caleb", "Cat", "Chad the Beardulous", "Chance", "Chris", "Jessica", "Jorge", "Joshua", "Justin", "Lui", "Stephen"]

wordbank.append(4)
print(wordbank)

num= int(input("Enter a number between 0 and 11\n"))

student_name= tlgstudents[num]
print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

randomstudent= random.choice(tlgstudents)
print(f"randomly selected student is {randomstudent}")

name= input("Please enter student name\n")

found= False
for student in tlgstudents:
    if student.lower() == name:
        found= True
        index= tlgstudents.index(student)
        print(f"{name} is located in this array at index {index}.")
        break

if not found:    
    print("The student is not in the list.")
