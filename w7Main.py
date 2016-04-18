def drawSquareAtSave(size,pos):
       t1.penup()
       t1.setpos(pos)
       t1.setheading(0)
       t1.pendown()
       for i in range(0,4):
           t1.fd(size)
           t1.right(90)
           x[i]=t1.pos()
   print x

def lab7():
   import turtle
   wn=turtle.Screen()
   t1=turtle.Turtle()
   pos=t1.pos
   x=list()
   for i in range(0,4):
          x.append(0)
   t1.pos()
   size = 100
   pos=(50,50)
   drawSquareAt(size,pos)

def main():

   lab7()

if __name__=="__main__":
    main()