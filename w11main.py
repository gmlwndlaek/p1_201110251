import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def keyup():
	t1.fd(50)
def keydown():
	t1.back(50)
def keyright():
	t1.right(90)
def keyleft():
	t1.left(90)
def mousegoto(x,y):
	t1.setpos(x,y)
def addKeys():
	wn.onkey(keyup,"Up")
	wn.onkey(keydown,"Down")
	wn.onkey(keyright,"Right")
	wn.onkey(keyleft,"Left")
	wn.onkey(wn.bye,"q")
def addMouse():
	wn.onclick(mousegoto)

def lab11():
	addKeys()
	addMouse()
	wn.listen()
	turtle.mainloop()
lab11()