from graphics import *
win=GraphWin('Circle',700,500)
win.setCoords(0.0, 0.0, 7.0, 5.0)
Text(Point(3.5,4.5),"Area of Circle").draw(win)

circ= Circle(Point(5.5,2.5), 1.3)
circ.setFill('Yellow')
circ.draw(win)

Text(Point(1,3),"Enter the radius:").draw(win)
input = Entry(Point(2,3), 5)
input.setText("0.0")
input.draw(win)

button = Text(Point(1,2.5),"Submit")
button.draw(win)
Rectangle(Point(0.72,2.4), Point(1.3,2.6)).draw(win)
win.getMouse()

r = eval(input.getText())
d = 2 * r
area = 3.14 * r ** 2

Text(Point(1,2),"Area of Circle= ").draw(win)
Text(Point(1.7,2),area).draw(win)

line1 = Line(Point(5.5,2.5),Point(5.5,3.8))
line1.draw(win)
line1.setFill('red')
line1.setArrow('last')

line2 = Line(Point(6.8,2.5),Point(4.2,2.5))
line2.draw(win)
line2.setFill('blue')
line2.setArrow('both')

Text(Point(5.9,3.1),"radius= ").draw(win)
Text(Point(6.2,3.1),r).draw(win)

Text(Point(5.5,2.4),"diameter= ").draw(win)
Text(Point(6,2.4),d).draw(win)

button.undraw()
q = Text(Point(1,2.5),"Quit")
q.draw(win)
win.getMouse()
win.close()

