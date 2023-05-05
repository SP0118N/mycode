#!/usr/bin/env python3

import json
import random
from flask import Flask, url_for, redirect, render_template, request, jsonify
import requests
# some missing imports, fixed those

# pulling JSON
with open("food.json","r") as example:
    data= json.load(example)

# start with Flask to represent a website
app= Flask(__name__) #name representing this whole code

@app.route("/data")
def get_data():
    return data

def fetch_food_image(query):
    api_key= "cs_n1mvrTDt7WwNpNuqCWBP2F_hHOCdtEGCa4k5J3rU"
    url= f"https://api.unsplash.com/search/photos?query={query}&client_id={api_key}"
    response= requests.get(url)

    if response.status_code == 200:
        data= response.json()
        if data["results"]:
            return data["results"][0]["urls"]["small"]
    return None

# first screen
@app.route("/")
def welcome(message=None):
    return render_template("frontpage.html", message=message)

@app.route("/food", methods=["POST", "GET"])
def get_food_name(): 
    if request.method == "POST":
        foodname= request.form["food_name"]
        foodlist=[]    
        for f in data:
            if foodname.lower() in f["food"].lower(): # wrong key, fixed
                image_url= fetch_food_image(foodname)
                return render_template("food.html" ,f=f, image=image_url)
        
        return redirect(url_for("welcome", message="No information for that food"))

    else:
        return redirect(url_for("welcome"))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224, debug=True)
                                    # adding debug=True means we don't have to keep stopping/starting the flask program every time we make a change :-P
