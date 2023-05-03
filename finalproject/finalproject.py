#!/usr/bin/env python3

import json
import random
from flask import Flask, url_for, redirect
                        # some missing imports, fixed those

# pulling JSON
with open("food.json","r") as example:
    data= json.load(example)

# start with Flask to represent a website
app= Flask(__name__) #name representing this whole code

# first screen
@app.route("/")
def welcome():
    return "Welcome to my final project"

# wrong input reroute
@app.route("/<foods>")
def redirection(foods): # here you're saying the variable "foods" needs passed into this function. You were missing the <angle brackets> on line 20. Also, need to change the name of this function to somethnig other than redirect
    return redirect(url_for("get_food_name",foodname= foods))


@app.route("/food/<foodname>")
def get_food_name(foodname): # the redirect on line 23 would have handled this, but if you went straight to "/food", then "foodname" would not have been defined. I added "<foodname> on line 26 to fix that.
    foodlist=[]    
    for f in data:
        if foodname.lower() in f["food"].lower(): # wrong key, fixed
            foodlist.append(f"Name: {f['food']}  Price: ${f['price']}  Ingredients: {', '.join(f['ingredient'])}") # wrong key, fixed
    return foodlist



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224, debug=True)
                                    # adding debug=True means we don't have to keep stopping/starting the flask program every time we make a change :-P
