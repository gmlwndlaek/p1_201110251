p1=raw_input("input player1")
p2=raw_input("input player2")

if p1=="r" :
    if p2=="r":
        print "draw"
    elif p2=="s":
        print "player1 win"
    elif p2=="p":
        print "player2 win"
    else:
        print "p2 error"
        
elif p1=="s":
    if p2=="r":
        print "player2 win"
    elif p2=="s":
        print "draw"
    elif p2=="p":
        print "player1 win"
    else:
        print "p2 error"
        
elif p1=="p":
    if p2=="r":
        print "player1 win"
    elif p2=="s":
        print "player2 win"
    elif p2=="p":
        print "draw"
    else:
        print "p2 error"
        
else:
    print "p1 error"
    
raw_input("if you want to exit, press enter")