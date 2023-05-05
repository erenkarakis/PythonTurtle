import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Interactive Turtle Learn")

turtle_object = turtle.Turtle()
turtle_object.color("green")

def turtle_forward():
    turtle_object.forward(50)

def rotate_angle_right():
    #turtle_object.right(10)
    turtle_object.setheading(turtle_object.heading() + 10)

def rotate_angle_left():
    #turtle_object.left(10)
    turtle_object.setheading(turtle_object.heading() - 10)

def clear_screen():
    turtle_object.clear()

def return_home():
    pen_up()
    turtle_object.home()
    pen_down()

def pen_up():
    turtle_object.penup()

def pen_down():
    turtle_object.pendown()


turtle_screen.listen()
turtle_screen.onkey(fun=turtle_forward, key="space")
turtle_screen.onkey(fun=rotate_angle_right, key="Down")
turtle_screen.onkey(fun=rotate_angle_left, key="Up")
turtle_screen.onkey(fun=clear_screen, key="c")
turtle_screen.onkey(fun=return_home, key="h")
turtle_screen.onkey(fun=pen_up, key="w")
turtle_screen.onkey(fun=pen_down, key="q")

turtle.mainloop()