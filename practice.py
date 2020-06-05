#screen size 620x540 approx.)
#wn.setup(width=650, height=650)
skk.forward(100)
skk.right(90)
skk.forward(100)
turtle.done()

import keyboard  # using module keyboard
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('d'):  # if key 'q' is pressed 
            skk.forward(200)
        elif keyboard.is_pressed('s'):
            skk.right(90)
            skk.forward(100)
        elif keyboard.is_pressed('a'):
            skk.right(90)
            skk.forward(100)
        elif keyboard.is_pressed('w'):
            skk.right(90)
            skk.forward(100)    
            break  # finishing the loop
    except:
        break 
import turtle
import keyboard

wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
skk = turtle.Turtle()
skk.forward(100)
skk.right(90)
turtle.done()
skk.position()



# Python program to draw  
# Rainbow Benzene


    
# using Turtle Programming 
import turtle 
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
t = turtle.Pen() 
turtle.bgcolor('black') 
for x in range(360): 
    t.pencolor(colors[x%6]) 
    t.width(x/100 + 1) 
    t.forward(x) 
    t.left(59)

    
paths=["up","down","right","left"]

while pamb.direction!= "stop":
    if pamb.distance(unda) <15:#works    
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        unda.goto(x, y)
        vaal=turtle.Turtle()
        vaal.color("green")
        vaal.shape("square")
        vaal.speed(0)
        vaal.penup()
        vaals.append(vaal)
        for index in range(len(vaals)-1, 0, -1):
            x = vaals[index-1].xcor()
            y = vaals[index-1].ycor()
            segments[index].goto(x, y)
            if len(vaals)==0:
                a = pamb.xcor()
                b = pamb.ycor()
                vaals[0].goto(a, b)
