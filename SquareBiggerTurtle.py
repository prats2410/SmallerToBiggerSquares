from turtle import *

speed(0)
colors=['pink','red','green','yellow','purple']
for i in range(500):
    pencolor(colors[i%5])
    forward(i+2)
    right(90)
