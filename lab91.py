#!/usr/bin/env python3
import wget
import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    #print(pokeapi)
    print(type(pokeapi))

    sprites= pokeapi["sprites"]["front_default"]
    print(sprites)
    wget.download(sprites, "/home/student/static")    

    #for m in pokeapi["moves"]:

   #     print(m["move"]["name"])
    
    #with Loop
    #games=0
    #for game in pokeapi["game_indices"]:
        #games+=1
    #print("Total number of games: ", games)
    
    #without Loop
    #games= len(pokeapi["game_indices"])
    #print("Total number of games: ",games)

main()

