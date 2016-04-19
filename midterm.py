import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.shape('turtle')

t1.left(90)
def drawWeed(size, pos):
    tracks=list()
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    for i in range(0,2):
        t1.fd(size)
        t1.right(180)
        tracks.append(t1.pos())
    return tracks

def drawWeed_list(tracks):
    t1.penup()
    t1.goto(tracks[1])
    t1.pendown()
    for i in range(0,2):
        t1.goto(tracks[i])
        
for i in range(0,90):
    t1.speed(50)
    if (i<15):
        x=-400+(i*20)
        y=-320
    elif (30>i>=15):
        x=-400+((i-15)*20)
        y=-280
    elif (45>i>=30):
        x=-400+((i-30)*20)
        y=-240
    elif (60>i>=45):
        x=-400+((i-45)*20)
        y=-200
    elif (75>i>=60):
        x=-400+((i-60)*20)
        y=-160
    elif (90>i>=75):
        x=-400+((i-75)*20)
        y=-120
    elif (i>90):
        x=-400+((i-90)*20)
        y=-80
    pos=(x, y)
    drawWeed_list(drawWeed(20, pos))
    


def drawNPC(size,pos):
    NPC=list()
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    for i in range(0,3):
        t1.fd(size)
        t1.left(120)
        NPC.append(t1.pos())
    return NPC

def drawNPC_list(NPC):
    t1.penup()
    t1.goto(NPC[1])
    t1.pendown()
    for i in range(3):
        t1.goto(NPC[i])
        
pos=(300,270)
drawNPC_list(drawNPC(30,pos))

def movefd():
    t1.fd(20)
def movebac():
    t1.back(20)
def movel():
    t1.left(45)
def mover():
    t1.right(45)
    
wn.onkey(movefd,"Up")
wn.onkey(movebac,"Down")
wn.onkey(movel,"Left")
wn.onkey(mover,"Right")
wn.listen()
t1.penup()
turtle.mainloop()


