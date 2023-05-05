import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Spiral Helix")

turtle_object = turtle.Turtle()
turtle_object.color("purple")

turtle_colors = ("pink", "red", "orange", "green", "blue", "purple", "yellow")

for i in range(15):
    turtle_object.color(turtle_colors[i % len(turtle_colors)])
    turtle_object.circle(10 * i)
    turtle_object.circle(-10 * i)
    turtle_object.left(i * 5)


turtle.done()