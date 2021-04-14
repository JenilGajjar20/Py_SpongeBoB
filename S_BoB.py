import turtle

turt = turtle.Turtle()
turt.pensize(5)

#body
turt.penup()
turt.goto(-70,-70)
turt.pendown()
turt.fillcolor('yellow')
turt.begin_fill()
turt.forward(200)
turt.left(90)
turt.forward(200)
turt.left(90)
turt.forward(200)
turt.left(90)
turt.forward(200)
turt.end_fill()

#brown_pants
turt.fillcolor('brown')
turt.begin_fill()
turt.forward(40)
turt.left(90)
turt.forward(200)
turt.left(90)
turt.forward(40)
turt.left(90)
turt.forward(200)
turt.left(90)
turt.end_fill()

#shirts
turt.fillcolor('white')
turt.begin_fill()
turt.forward(20)
turt.left(90)
turt.forward(200)
turt.left(90)
turt.forward(20)
turt.left(90)
turt.forward(200)
turt.end_fill()

turt.penup()

#tie
turt.left(90)
turt.forward(18)
turt.left(90)
turt.forward(100)
turt.fillcolor('red')
turt.begin_fill()
turt.pencolor('red')
turt.pendown()
turt.circle(7)
turt.end_fill()

turt.penup()

#eye-1
turt.pencolor('black')
turt.goto(75,50)
turt.pendown()
turt.fillcolor('white')
turt.begin_fill()
turt.circle(25)
turt.end_fill()

turt.fillcolor('black')
turt.penup()
turt.goto(80,60)
turt.begin_fill()
turt.circle(10)
turt.end_fill()

#eye-2
turt.penup()
turt.pencolor('black')
turt.goto(-15,50)
turt.pendown()
turt.fillcolor('white')
turt.begin_fill()
turt.circle(25)
turt.end_fill()

turt.fillcolor('black')
turt.penup()
turt.goto(-10,60)
turt.begin_fill()
turt.circle(10)
turt.end_fill()

#smile
turt.penup()
turt.goto(-10,0)
turt.pendown()
turt.pensize(5)
turt.right(90)
turt.fillcolor('red')
turt.begin_fill()
turt.circle(40,180)
turt.left(90)
turt.forward(80)
turt.end_fill()

#teeths
turt.fillcolor('white')
turt.begin_fill()
turt.left(180)
turt.forward(25)
turt.right(90)
turt.forward(15)
turt.left(90)
turt.forward(10)
turt.left(90)
turt.forward(15)
turt.end_fill()

turt.fillcolor('white')
turt.begin_fill()
turt.right(90)
turt.forward(10)
turt.right(90)
turt.forward(15)
turt.left(90)
turt.forward(10)
turt.left(90)
turt.forward(15)
turt.end_fill()


style = ('Courier', 50, 'bold')
turt.penup()
turt.pensize(5)
turt.goto(-240, -240)
turt.write("SpongeBob", font=style)

turtle.done()