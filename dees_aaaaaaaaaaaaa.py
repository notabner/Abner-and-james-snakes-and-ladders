import random
import os

p1d = 0
p2d = 0
p1 = 0
p2 = 0
turn = 0

y0 = ["01","02","03","04","05","06","07","08","09","10"]
y1 = ["20","19","18","17","16","15","14","13","12","11"]
y2 = ["21","22","23","24","25","26","27","28","29","30"]
y3 = ["40","39","38","37","36","35","34","33","32","31"]
y4 = ["41","42","43","44","45","46","47","48","49","50"]
y5 = ["60","59","58","57","56","55","54","53","52","51"]
y6 = ["61","62","63","64","65","66","67","68","69","70"]
y7 = ["80","79","78","77","76","75","74","73","72","71"]
y8 = ["81","82","83","84","85","86","87","88","89","90"]
y9 = ["100","99","98","97","96","95","94","93","92","91"]

ylist = [y9,y8,y7,y6,y5,y4,y3,y2,y1,y0]

# Define snakes and ladders
snakes = [random.randint(1, 100) for _ in range(5)]  # List of snake head positions
ladders = {20: 40, 35: 70, 50: 80, 60: 90, 80: 100}  # Ladder positions and where they take you

def dice_rollp1(p1):
    p1 = random.randint(1, 6)
    return p1

def dice_rollp2(p2):
    p2 = random.randint(1, 6)
    return p2

def findPlayerPos(y):
    if int(y) == p1:
        return "P1"
    elif int(y) == p2:
        return "P2"
    else:
        return y

def printTable():
    for i in ylist:
        if not i == y9:
            printY = " "
        else:
            printY = ""
        
        for y in i:
            plrPos = findPlayerPos(y)
            printY += plrPos
            printY += "|  "
        print(printY)

# Main game loop
while True:
  if p1 >= 100:
    print("player 1 wins")
  elif p2 >=100:
    print("player 2 wins")
  else:
    print("Snakes positions:", snakes)
    print("Ladders positions:", ladders)
    
  
    if turn == 0:
      p1d = dice_rollp1(p1d)
      turn = turn + 1
      print("Player 1 rolled", p1d)
      p1 = p1 + p1d
      print("player 1 is on", p1)
      input("Press enter to roll")
      # Check for snakes
      if p1 in snakes:
        p1 = p1 - random.randint(1, 10)
        print("Haha loser, you hit a snake! P1 is now on", p1)
        input("Press enter to roll")
            # Check for ladders
      if p1 in ladders:
        p1 = p1 + random.randint(1,10)
        print("You climbed a ladder! P1 is now on", p1)
        print("Player 1 is on", p1)
        input("Press enter to roll")
    elif turn == 1:
      p2d = dice_rollp2(p2d)
      turn = turn - 1
      print("Player 2 rolled", p2d)
      p2 = p2 + p2d
      print("player2 is now on", p2)
      input("Press enter to roll")
  # Check for snakes
      if p2 in snakes:
        p2 = p2 - random.randint(1, 10)
        print("Haha loser, you hit a snake! P2 is now on", p2)
        input("Press enter to roll")
            # Check for ladders
      if p2 in ladders:
        p2 = p2 + random.randint(1,10)
        print("You climbed a ladder! P2 is now on", p2)
        print("Player 2 is on", p2)
        input("Press enter to roll")
    
    os.system('clear')
    printTable()
