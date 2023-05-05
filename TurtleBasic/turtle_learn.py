import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Python Turtle")

'''
turtle_instance = turtle.Turtle()
turtle_instance.forward(100)
turtle.done()
'''
turtle_instance = turtle.Turtle()

'''
#square
for i in range(4):
    turtle_instance.forward(200)
    turtle_instance.left(90)
'''

#star
for i in range(8):
    turtle_instance.forward(200)
    turtle_instance.left(135)

turtle.done()


