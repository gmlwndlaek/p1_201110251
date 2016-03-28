import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def makeSwirlSquare(size, bigger, sides, angle):
    t1.home()
    t1.clear()
    for i in range(0,sides):
        if i%2:
            size=size+bigger
        else:
            size
        t1.fd(size)
        t1.right(angle)
        
makeSwirlSquare(10, 10, 10, 90)

wn.exitonclick()