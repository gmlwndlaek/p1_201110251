import turtle 
wn=turtle.Screen() 
t1=turtle.Turtle() 
 
def drawSquareAtSave(size,pos): 
    tracks=list() 
    t1.penup() 
    t1.setpos(pos) 
    for i in range(0,4): 
        t1.fd(size) 
        t1.left(90) 
        tracks.append(t1.pos()) 
    return tracks 

def lab7(): 
    size=100 
    pos=t1.pos() 
    mytracks=drawSquareAtSave(size,pos) 
    drawSquareFront_list(mytracks) 
    print mytracks 

def main(): 
    lab7() 
    
def drawSquareFront_list(tracks): 
    t1.penup() 
    t1.goto(tracks[3]) 
    t1.pendown() 
    for i in range(4): 
        t1.goto(tracks[i])
        
if __name__=="__main__":
    main() 