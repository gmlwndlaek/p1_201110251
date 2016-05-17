import turtle
import math

wn=turtle.Screen()

t1=turtle.Turtle()

coord=[(100,100),(200,200)]


def isInRectangle(curpos,coord):
    xs=coord[0][0]
    xe=coord[1][0]
    ys=coord[0][1]
    ye=coord[1][1]

    if xs <= curpos[0] <= xe and ys <=curpos[1] <= ye:
        return True
    else:
        return False


line1=[(50,0),(150,0)]


def isOnLine(point):
    x1=line1[0][0]-1
    y1=line1[0][1]-1
    x2=line1[1][0]+1
    y2=line1[1][1]+1
    if isInRectangle(point,[(x1,y1),(x2,y2)]):
        return True
    else:
        return False


def isIncircle(curpos):
    radius=50
    pos=(-50,50)
    if math.sqrt(math.pow(curpos[0]-pos[0],2) + math.pow(curpos[1]-pos[1],2))<=radius:
        return True
    else:
        return False
       

def where_cursor(curpos):
    if isInRectangle(curpos,coord):
        t1.pencolor("Red")
        t1.write("this")
    elif isOnLine(curpos):
        t1.pencolor("Purple")
        t1.write("this")
    elif isIncircle(curpos):
        t1.pencolor("Blue")
        t1.write("circle")
    else:
        t1.pencolor("black")
        t1.write("no")

        
def move_up():
    t1.fd(50)
    curpos=t1.pos()
    where_cursor(curpos)
    


def move_down():
    t1.back(50)
    curpos=t1.pos()
    where_cursor(curpos)



def move_left():
    t1.left(90)

    

def move_right():
    t1.right(90)


    
def mousegoto(x,y):
    t1.setpos(x,y)
    curpos=t1.pos()
    where_cursor(curpos)


def exit():
    wn.bye()


def byeBye():
    wn.onkey(exit,"q")


    
def addkeys():
    wn.onkey(move_up,"Up")
    wn.onkey(move_down,"Down")
    wn.onkey(move_left,"Left")
    wn.onkey(move_right,"Right")

    
def addMouse():
    wn.onclick(mousegoto)
    

def lab11():
    addkeys()
    addMouse()
    byeBye()
    wn.listen()
    turtle.mainloop()


lab11()