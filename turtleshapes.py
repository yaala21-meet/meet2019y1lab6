import turtle

x = 1
turtle.pensize = 2

while True: 
    while x<50:
        if x<20:
            turtle.speed(2)
        else:
            turtle.speed(x/5)
        turtle.left(60)
        turtle.forward(x*10)
        x = x + 1

    turtle.right(180)

    while x>0:
        if x<20:
            turtle.speed(2)
        else:
            turtle.speed(x/5)
        turtle.pencolor("white")
        turtle.forward(x*10 - 10)
        turtle.right(60)
        x = x - 1

    turtle.pencolor("black")
