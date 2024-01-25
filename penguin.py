import turtle as t

t.setheading(270)
t.begin_fill()
t.circle(50,180)
t.forward(80)
t.circle(50,180)
t.forward(80)
t.end_fill()

t.fillcolor("white")
t.goto(10,0)
t.begin_fill()
t.circle(40)
t.end_fill()

t.setheading(0)
t.goto(30,80)
t.begin_fill()
t.circle(20)
t.end_fill()

t.goto(70,80)
t.begin_fill()
t.circle(20)
t.end_fill()

t.shape("circle")
t.fillcolor("black")
t.penup()
t.goto(30,100)
t.stamp()
t.goto(70,100)
t.stamp()

t.setheading(270)
t.shape("triangle")
t.fillcolor("orange")
t.goto(50,70)
t.stamp()

t.setheading(0)
t.fillcolor("black")
t.pencolor("white")
t.goto(0,50)
t.stamp()
t.setheading(180)
t.goto(100,50)
t.stamp()

t.shape("square")
t.fillcolor("orange")
t.goto(35,-50)
t.stamp()
t.goto(65,-50)
t.stamp()



t.done()
