#!/usr/bin/env python3
import pprint
import requests

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def name_finder(got_list):
    names=[] #empty list
    for i in got_list:
        r= request.get(i)
        decodedjson= r.json()
        names.append(decodedjson.get("name"))
    return names

def main():
    userinput= input("pick a number between 1 and 1000")

    gotresp = requests.get(AOIF_CHAR + userinput)

    
    got_dj = gotresp.json()
    pprint.pprint(got_dj)

    print("This character belongs to the following houses:")
    for i in name_finder(got_dj.get("allegiances")):
        print(i)

    print("This character appears in the following books:")
    for i in name_finder(got_dj.get("books")):
        print(i)

if __name__ == "__main__":
    main()
