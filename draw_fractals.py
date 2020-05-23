import turtle

def draw_triangles(turtle_draw):
    turtle_draw.begin_fill()
    for _ in range(1, 4):
        turtle_draw.forward(50)
        turtle_draw.left(120)
    turtle_draw.end_fill()

def move_turtle(turtle_draw):
    turtle_draw.forward(50)
    turtle_draw.right(60)

def draw_small_fractal(turtle_draw):
    for _ in range(1, 4):
        for _ in range(1, 3):
            draw_triangles(turtle_draw)
            turtle_draw.left(60)
            move_turtle(turtle_draw)

        turtle_draw.right(60)
        move_turtle(turtle_draw)
        draw_triangles(turtle_draw)
        turtle_draw.right(120)
        turtle_draw.forward(50)


def draw_fractal():
    window = turtle.Screen()
    window.bgcolor("white")

    squirtle = turtle.Turtle()
    squirtle.shape("turtle")
    squirtle.color("blue", "green")
    squirtle.speed(2)
    draw_small_fractal(squirtle)
    squirtle.forward(200)
    draw_small_fractal(squirtle)
    squirtle.back(100)
    squirtle.left(120)
    squirtle.forward(200)
    squirtle.right(120)
    squirtle.forward(100)
    draw_small_fractal(squirtle)

    window.exitonclick()

draw_fractal()
