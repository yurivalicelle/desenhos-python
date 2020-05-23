import turtle

def draw_diamond(turtle_draw):
    for _ in range(1, 3):
        turtle_draw.forward(100)
        turtle_draw.right(45)
        turtle_draw.forward(100)
        turtle_draw.right(135)

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")

    squirtle = turtle.Turtle()
    squirtle.shape("turtle")
    squirtle.color("blue")
    squirtle.speed(10)
    for _ in range(1, 37):
        draw_diamond(squirtle)
        squirtle.right(10)

    squirtle.right(90)
    squirtle.forward(300)

    window.exitonclick()

draw_flower()
