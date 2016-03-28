import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

sel=raw_input("F or C:")
print sel
temp=raw_input("please enter temperature:")
temp=float(temp)
 
if(sel=='F'):
    print ((temp-32)/1.8,"C")
elif(sel=='C'):
    print ((temp*1.8)+32,"F")
else:
    print "Entered again please"

wn.exitonclick()