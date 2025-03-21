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

def dice_rollp1(p1d):
    p1d = random.randint(1, 6)
    return p1

def dice_rollp2(p2d):
    p2d = random.randint(1, 6)
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
while True:
 
    snakes = random.randint(1, 100)
    snake1 = random.randint(1, 100)
    snake2 = random.randint(1, 100)
    snake3 = random.randint(1, 100)
    snake4 = random.randint(1, 100)
    
    print(snakes, snake1, snake2, snake3, snake4)

    if turn == 0:
        p1d = dice_rollp1(p1d)
        turn = turn + 1
        print("player 1 rolled", p1d)
        p1 = p1 + p1d
        if p1 == snakes or p1 == snake1 or p1 == snake2 or p1 == snake3 or p1 == snake4:
            p1 = p1 - random.randint(1, 10)
            print("haha loser u hit a snake, p1 is now on", p1)
        print("player 1 is on", p1)
    elif turn == 1:
        p2d = dice_rollp2(p2d)
        turn = turn - 1
        print("player 2 rolled", p2d)
        p2 = p2 + p2d
        if p2 == snakes or p2 == snake1 or p2 == snake2 or p2 == snake3 or p2 == snake4:
            p2 = p2 - random.randint(1, 10)
            print("haha loser u hit a snake, p2 is now on", p2)
        print("player 2 is on", p2)

    input("press enter to roll")
    os.system('clear')
    printTable()
