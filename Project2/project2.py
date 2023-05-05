#!/usr/bin/env python3

def showInstructions():
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  teleport [room]
  fight
  answer [riddle question]
  exit
''')

def showStatus():
  print('---------------------------')
  print('You are in the ' + currentRoom)
  print('Inventory : ' + str(inventory))
  if "item" in rooms[currentRoom]:
    items=', '.join(rooms[currentRoom]['item'])
    print(f'You see a ' + items)
  print("---------------------------")

# exit game definition
def exitGame():
  print("Thank you for playing!")
  exit()
#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : ['key','beer']
                },
            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : ['monster']
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'north' : 'Guest Room',
                  'south': 'Garden',
                  'item' : ['potion']
               },
            'Garden' : {
                  'north' : 'Dining Room'
               },
            'Master Bedroom': {
                  'south' : 'Hall',
                  'east'  : 'Guest Room',
                  'item'  : ['gun','bullet','sword'],
                  'door'  : 'Trapdoor'
                  },
            'Guest Room' : {
                  'south' : 'Dining Room',
                  'west'  : 'Master Bedroom',
            }
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
      move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
  else:
    print('You can\'t go that way!')
  #if they type 'get' first
  
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #remove the item from the room
      rooms[currentRoom]['item'].remove(move[1])
      #in case item in the room is empty
      if not rooms[currentRoom]['item']:
        del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
  else:
      #tell them they can't get it
    print('Can\'t get ' + move[1] + '!')
      
   #if they type 'teleport' first
  if move[0] == 'teleport':
    if move[1] in rooms[currentRoom]:
      currentRoom= move[1]  
  else:
      print('That room does not exist')

  # if they type 'exit' first
  if move == 'exit':
    exitGame()
    
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break