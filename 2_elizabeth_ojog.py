import turtle 


screen = turtle.Screen()
t = turtle.Turtle()


def koch_side(n):
    if n == 0:
        t.forward(20)
    else:
        for angle in [60, -120, 60, 0]:  
            koch_side(n - 1)
            t.left(angle)

# ask user for recursion level
level = int(input("Enter recursion level (e.g. 0–4): "))

# koch_side(2)
for _ in range(3):
    koch_side(level)
    t.right(120)

screen.mainloop()

