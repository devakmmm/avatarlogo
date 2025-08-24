# Avatar-inspired glowing "A" with Python turtle (original design)
# Run locally: python3 this_file.py
import turtle as t
from math import sin, cos, pi

t.colormode(255)
t.bgcolor("black")
t.speed(0)
t.hideturtle()

def poly(points, width, color):
    t.pensize(width)
    t.pencolor(color)
    t.penup()
    t.goto(points[0])
    t.pendown()
    for p in points[1:]:
        t.goto(p)
    t.penup()

def bezier(p0, p1, p2, p3, steps=220):
    pts=[]
    for i in range(steps+1):
        t_ = i/steps
        mt = 1 - t_
        x = (mt**3)*p0[0] + 3*(mt**2)*t_*p1[0] + 3*mt*(t_**2)*p2[0] + (t_**3)*p3[0]
        y = (mt**3)*p0[1] + 3*(mt**2)*t_*p1[1] + 3*mt*(t_**2)*p2[1] + (t_**3)*p3[1]
        pts.append((x,y))
    return pts

S = 280   # scale
cx, cy = 0, -40

def R(u,v): return (cx + u*S, cy + v*S)

# Curved legs + crossbar
L0,L1,L2,L3 = R(-0.55,0.9), R(-0.65,0.2), R(-0.25,-0.9), R(0.0,-1.05)
R0,R1,R2,R3 = R(0.55,0.9),  R(0.65,0.2),  R(0.25,-0.9),  R(0.02,-1.05)
C0,C1,C2,C3 = R(0.5,-0.05), R(0.1,0.15), R(-0.4,0.1),   R(-0.65,-0.05)
F0,F1,F2,F3 = R(-0.1,-1.05), R(-0.2,-1.2), R(-0.4,-1.0), R(-0.2,-0.9)

left_leg   = bezier(L0,L1,L2,L3,260)
right_leg  = bezier(R0,R1,R2,R3,260)
crossbar   = bezier(C0,C1,C2,C3,220)
flourish   = bezier(F0,F1,F2,F3,140)

paths = [left_leg, right_leg, crossbar, flourish]

# Fake "glow" by drawing thicker, darker blues first, then thinner bright cyan on top
glow_layers = [
    (36, (10, 90, 220)),
    (24, (30,140,255)),
    (14, (60,200,255)),
    (6,  (170,240,255)),
]

for w,col in glow_layers:
    for pts in paths:
        poly(pts, w, col)

# Add a few spark points along the crossbar
t.pencolor(255,255,255)
for i in range(0, len(crossbar), 30):
    t.penup(); t.goto(crossbar[i]); t.pendown()
    t.dot(6, (255,255,255))
    t.dot(12, (120,220,255))

t.done()