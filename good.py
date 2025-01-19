import turtle 
t = turtle.Turtle()
s = turtle.Screen()
color = ['red', 'green', 'black', 'purple', 'white', 'blue']
s.bgcolor('black')
t.speed(10)
t.hideturtle()
while True:
    for i in range(200):
        t.pencolor(color[i%len(color)])
        t.width(i/100 + 1)
        t.forward(i)
        t.left(59)
    t.right(239)    
    for i in range(200, 0, -1):
        t.pencolor('black')
        t.width(i/100 + 7)
        t.forward(i)
        t.right(59)
