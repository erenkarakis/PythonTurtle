import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("blue")
turtle_screen.title("Shrinking Square")
turtle_instance = turtle.Turtle()
turtle_instance.color("red")

edgeLength = 200
reductionSize = 20

def square(edgeLength=200):
    for i in range(4):
        turtle_instance.forward(edgeLength)
        turtle_instance.left(90)
        edgeLength -= 5

square(300)
square(200)
square(100)
square(50)
square(10)



turtle.done()


