#!/usr/bin/env python3

import requests
import html
import random

def main():
    # Get difficulty input
    difficulty=input("Select a difficulty: Easy, Medium, Hard \n >").lower()
    if difficulty not in ["easy","medium","hard"]:
        print("Invalid input")
        return
    
    # Get number of question
    question_number=input("How many questions you want?\n >")
    try:
        question_number=int(question_number)
    except ValueError:
        print("error")
        return

    # Set type of questions
    typeOfQuestion= input("Select type: Multiple or True/False\n >").lower()
    if typeOfQuestion not in ["multiple", "boolean"]:
        print("Invalid choice")
        return
    
    # Set URL accodring to user input
    URL="https://opentdb.com/api.php?amount={}&difficulty={}&type={}".format(question_number,difficulty,typeOfQuestion)
    
    # Get json
    data= requests.get(URL).json()

    # Questions and Answer
    question= html.unescape(data["results"][0]["question"])
    correct_answer= html.unescape(data["results"][0]["correct_answer"])
    incorrect_answer= [html.unescape(answer) for answer in data["results"][0]["incorrect_answers"]]

    answer_choices= incorrect_answer + [correct_answer]
    random.shuffle(answer_choices)

    # Print it
    print(question)
    for i, choice in enumerate(answer_choices):
        print("{}. {}".format(i+1, choice))
        
    # User input for the answer, use for loop for giving 3 chances
    for i in range(3):
        guess= input("What is your answer?\n >")
        try:
            guess= int(guess)
            if guess < 1 or guess > len(answer_choices):
                raise ValueError()
        except ValueError:
            print("Invalid input")
            continue

        if answer_choices[guess-1] == correct_answer:
            print("This is the correct answer.")
            break
        else:
            print(" Wrong answer")
            if i<2:
                print("you have",2-i,"guess remaining.")
            else:
                print("You are out of your chance. The correct answer is: ", correct_answer)


if __name__ == "__main__":
    main()
