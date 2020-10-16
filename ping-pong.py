import turtle

win = turtle.Screen()
win.title("Pong game")
win.bgcolor("black")
win.setup(width=800, height=600)

win.tracer(0)   #prevents auto-update of screen

scorea=0
scoreb=0
#paddle A
paddlea = turtle.Turtle()
paddlea.speed(0)    #speed of animation
paddlea.shape("square")
paddlea.shapesize(stretch_wid=5,stretch_len=1)
paddlea.color("white")
paddlea.penup()     #penup/down for not-draw/draw
paddlea.goto(-350,0)

#paddle B
paddleb = turtle.Turtle()
paddleb.speed(0)    #speed of animation
paddleb.shape("square")
paddleb.shapesize(stretch_wid=5,stretch_len=1)
paddleb.color("white")
paddleb.penup()     #penup/down for not-draw/draw
paddleb.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)    #speed of animation
ball.shape("square")
ball.color("white")
ball.penup()     #penup/down for not-draw/draw
ball.goto(0,0)
ball.dx=0.15   #moves ball at speed of 2pixels
ball.dy=0.15

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Abhineet:0  Rishav:0",align="center",font=("Courier",24,"normal"))

def paddlea_up():
    y=paddlea.ycor()        #ycoe return the y coedinate
    y+=20
    paddlea.sety(y)         #sets y cordinate

def paddlea_down():
    y=paddlea.ycor()    
    y-=20
    paddlea.sety(y)

def paddleb_up():
    y=paddleb.ycor()        
    y+=20
    paddleb.sety(y)         

def paddleb_down():
    y=paddleb.ycor()    
    y-=20
    paddleb.sety(y)
    

win.listen()                #listens keyboard input
win.onkeypress(paddlea_up,"w")      #on w press call paddlea_up  
win.onkeypress(paddlea_down,"s")
win.onkeypress(paddleb_up,"Up")      
win.onkeypress(paddleb_down,"Down")

while True:
    win.update()
    
    #ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        scorea+=1
        pen.clear()
        pen.write("Abhineet:{}  Rishav:{}".format(scorea,scoreb),align="center",font=("Courier",24,"normal"))
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        scoreb+=1
        pen.clear()
        pen.write("Abhineet:{}  Rishav:{}".format(scorea,scoreb),align="center",font=("Courier",24,"normal"))
        
    #paddle and ball collision
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddleb.ycor()+40 and ball.ycor()>paddleb.ycor()-40):
        ball.setx(340)
        ball.dx*=-1
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddlea.ycor()+40 and ball.ycor()>paddlea.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1
        
