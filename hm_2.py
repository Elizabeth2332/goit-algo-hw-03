import turtle 
import argparse


screen = turtle.Screen()
t = turtle.Turtle()


# t.forward(50)
# t.left(60)
# t.forward(50)
# t.left(-120)
# t.forward(50)
# t.left(60)
# t.forward(50)


def koch_side(n):
    if n == 0:
        t.forward(50)
    else:
        for angle in [60, -120, 60, 0]:  
            koch_side(n - 1)
            t.left(angle)

# koch_side(2)

for _ in range(3):
    koch_side(3)
    t.right(120)
screen.mainloop()

