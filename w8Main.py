import turtle
wn=turtle.Screen()
wn.bgpic("myMaze.gif")
t1=turtle.Turtle()

def saveTracks():
    tracks=list()
    t1.penup()
    t1.setpos(-400,300)
    tracks.append(t1.pos())
    t1.pendown()
    t1.pencolor("Red")
    t1.right(90)
    t1.fd(400)
    tracks.append(t1.pos())
    t1.backward(150)
    tracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.back(150)
    tracks.append(t1.pos())
    t1.right(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.left(90)
    t1.right(90)
    t1.right(90)
    t1.fd(200)
    tracks.append(t1.pos())
    t1.fd(300)
    tracks.append(t1.pos())
    t1.back(100)
    tracks.append(t1.pos())
    t1.left(90)
    t1.fd(200)
    tracks.append(t1.pos())
    return tracks


def replayTracks(tracks):
    t1.penup()
    t1.setpos(tracks[0])
    t1.pendown()
    for i in range(0,11):
        t1.goto(tracks[i])


def lab8():
    tracks=saveTracks()
    replayTracks(tracks)

def main():
    lab8()

if __name__=="__main__":
    main()

raw_input()
    
    