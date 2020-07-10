import turtle
turtle.bgcolor("pink")
def rect(color):
    i = 0
    turtle.begin_fill()
    turtle.down()
    turtle.color(color)
    while i< 4:
        turtle.forward(40)
        turtle.left(90)
        i += 1
    turtle.up() 
    turtle.end_fill()
def tforward():
    turtle.forward(40)
def dhorizontal(inverted):
    if(inverted):
        for i in range(0, 8):
            if(i > 0 and i % 2 != 0):
                tforward()
                rect("white")
            if(i > 0 and i % 2 == 0):
                tforward()
                rect("black")
            if(i == 0):
                rect("black")
    else:
        for i in range(0, 8):
            if(i > 0 and i % 2 != 0):
                tforward()
                rect("black")
            if(i> 0 and i% 2 == 0):
                tforward()
                rect("white")
            if(horizontal == 0):
                rect("white")

for j in range(0, 8):
    turtle.setx(0)
    turtle.sety(40 * j)
    if(j % 2 == 0):
        dhorizontal(inverted=True)
    else:
        dhorizontal(inverted=False)

turtle.setx(0)
turtle.sety(0)
turtle.done()
