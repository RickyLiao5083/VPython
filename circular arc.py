#f(x)=(15π²+60-sqrt(225π⁴-1800π²+240πx-4x²+3600))/2
from vpython import *
m,g,size,h,d=1,980,3,60,30*pi
A,B=vec(0,h,0),vec(30*pi,0,0)

scene = canvas(width=500, align='left', center=(A+B)/2, background=vec(0.5, 0.5, 0))
ball = sphere(radius = size, pos=A, color=color.red, make_trail = True, trail_radius = 1)
x_plane = box(length=100, height=0.3, width=5, color=color.blue, pos=vec(30*pi/2,0,0))
y_plane = box(length=0.3, height=65, width=5, color=color.blue, pos=vec(0,30,0))
a_x = graph(width=400, align='left', xtitle='x', ytitle='a_t', background=vec(1, 1, 1))
c_a_x = gcurve(color=color.cyan, graph=a_x)
a_t = graph(width=400, align='left', xtitle='t', ytitle='a_t', background=vec(1, 1, 1))
c_a_t = gcurve(color=color.cyan, graph=a_t)
ball.v=vec(0,0,0)

def a_n(x,y):
    return 2*g*(60-ball.pos.y)/((15*pi**2+60)/2)
def a_t(x,y):
    return g*(30*pi-ball.pos.x)/((15*pi**2+60)/2)

t=0
dt=0.0001
while True:
    rate(2000)
    ball.a=a_n(ball.pos.x,ball.pos.y)*vec(30*pi-ball.pos.x,(15*pi**2+60)/2-ball.pos.y,0).norm()+a_t(ball.pos.x,ball.pos.y)*vec((15*pi**2+60)/2-ball.pos.y,-30*pi+ball.pos.x,0).norm()
    ball.v+=ball.a*dt
    ball.pos+=ball.v*dt
    t+=dt
    at=a_t(ball.pos.x,ball.pos.y)*vec((15*pi**2+60)/2-ball.pos.y,-30*pi+ball.pos.x,0).norm()
    c_a_x.plot(pos=(ball.pos.x,mag(at)))
    c_a_t.plot(pos=(t,mag(at)))
    if ball.pos.y<=0:
        break

print(t)

