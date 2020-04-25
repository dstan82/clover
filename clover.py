from turtle import *

def curvemove():
    for i in range(250):
        right(1)
        forward(3)

color('green','lightgreen')       
begin_fill()
pensize(10)

right(90)

for i in range(4):
	curvemove()
	left(160)

pensize(20)
forward(1000)

end_fill()
done()
