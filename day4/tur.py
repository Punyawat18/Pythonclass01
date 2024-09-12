m = [50]
print(type(m[0]))
p = 1
import turtle
turtle.speed(100)

turtle.right(135)
while True:
    for a in range(len(m)):
        print(a)
        for x in range(5):
            print(a)
            for i in range(5):
                print(a)
                turtle.color("blue")
                turtle.forward(m[a])
                turtle.color("pink")
                turtle.forward(m[a])
                turtle.right(144)
                print(m[a])
            turtle.forward(4 * m[a])
            print((4 * m[a]))
            turtle.right(144)
    m.append(2 * m[len(m) - 1])
    print(m)

turtle.done()