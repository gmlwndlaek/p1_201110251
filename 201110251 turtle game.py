import turtle
import random
t1=turtle.Turtle()
monster=turtle.Turtle()
monster2=turtle.Turtle()
monster3=turtle.Turtle()
wn=turtle.Screen()

def jungle():
    t1.penup()
    t1.goto(-440,-370)
    t1.pendown()
    t1.fd(900)
    t1.left(90)
    t1.fd(500)
    t1.left(90)
    t1.fd(900)
    t1.left(90)
    t1.fd(500)
    t1.penup()
    t1.goto(-440,370)

jungle()


def setting():
    t1.pencolor('red')
    monster.shape('turtle')
    monster.speed(2)
    monster2.shape('turtle')
    monster2.speed(2)
    monster3.shape('turtle')
    monster3.speed(2)
def setEvent():
    wn.onkey(keyUp,"Up")
    wn.onkey(keyLeft,"Left")
    wn.onkey(keyRight,"Right")
    wn.onkey(keyDown,"Down")
    wn.onkey(keyShoot,"space")
    wn.listen()
def keyShoot():
    t3=turtle.Turtle()
    t3.ht()
    t3.goto(t1.pos())
    t3.seth(t1.heading())
    t3.st()
    t3.speed(10)
    for i in range(0,20):
        t3.fd(10)
        if(t3.distance(monster) <20):
                monster.pencolor('red')
        if(t3.distance(monster2) <20):
                monster2.pencolor('red')
        if(t3.distance(monster3) <20):
                monster3.pencolor('red')
                
def keyUp():
    t1.fd(50)
def keyLeft():
    t1.left(30)
def keyRight():
    t1.right(30)
def keyDown():
    t1.back(50)
    

def monsterTurtle():
    point=0
    counter=0
    monster.penup()
    monster2.penup()
    monster3.penup()
    while True:
        monster.seth(monster.heading()+random.randint(-90-(int)(counter/10),90+(int)(counter/10)))
        monster.fd(random.randint(20+(int)(counter/10),50+(int)(counter/10)))
        print(monster.heading())
        if monster.pos()[0]<-440:
            monster.goto(-440,monster.pos()[1])
        if monster.pos()[0]>560:
            monster.goto(560,monster.pos()[1])
        if monster.pos()[1]<-370:
            monster.goto(monster.pos()[0],-370)
        if monster.pos()[1]>130:
            monster.goto(monster.pos()[0],130)
        counter+=1
            
        if monster.distance(t1)<30:
            monster.write("monster Caught")
            point=point+1
            t1.write(point)

            
        if monster.pencolor()== 'red':
            monster.write("monster shot")
            point=point+2
            t1.write(point)
            monster.pencolor('black')

            
            
        monster2.seth(monster.heading()+random.randint(-90-(int)(counter/10),90+(int)(counter/10)))
        monster2.fd(random.randint(20+(int)(counter/10),50+(int)(counter/10)))
        print(monster2.heading())
        if monster2.pos()[0]<-440:
            monster2.goto(-440,monster2.pos()[1])
        if monster2.pos()[0]>560:
            monster2.goto(560,monster2.pos()[1])
        if monster2.pos()[1]<-370:
            monster2.goto(monster2.pos()[0],-370)
        if monster2.pos()[1]>130:
            monster2.goto(monster2.pos()[0],130)
        counter+=1
            
        if monster2.distance(t1)<30:
            monster2.write("monster2 Caught")
            point=point+1
            t1.write(point)


            
        if monster2.pencolor()== 'red':
            monster2.write("monster2 shot")
            point=point+2
            t1.write(point)
            monster2.pencolor('black')


            
        
        monster3.seth(monster.heading()+random.randint(-90-(int)(counter/10),90+(int)(counter/10)))
        monster3.fd(random.randint(20+(int)(counter/10),50+(int)(counter/10)))
        print(monster3.heading())
        if monster3.pos()[0]<-440:
            monster3.goto(-440,monster3.pos()[1])
        if monster3.pos()[0]>560:
            monster3.goto(560,monster3.pos()[1])
        if monster3.pos()[1]<-370:
            monster3.goto(monster3.pos()[0],-370)
        if monster3.pos()[1]>130:
            monster3.goto(monster3.pos()[0],130)
        counter+=1
            
        if monster3.distance(t1)<30:
            monster3.write("poison monster3 Caught YOU DIE")
            point=point-10
            t1.write(point)


        if monster3.pencolor()== 'red':
            monster3.write("poison monster shot!")
            point=point-2
            t1.write(point)
            monster3.pencolor('black')
            
        if point > 10:
            t1.write("YOU WIN!")
            break
        if point < -5:
            t1.write("YOU LOSE")
            break

    return point
    

def gameplay():
    setting()
    setEvent()
    monsterTurtle()
    turtle.mainloop()
    
gameplay()




