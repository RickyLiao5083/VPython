#f(x)=-2/pi*x+60
from vpython import *
m,g,size,h,d=1,980,3,60,30*pi
A,B=vec(0,h,0),vec(30*pi,0,0)

scene = canvas(width=500, align='left', center=(A+B)/2, background=vec(0.5, 0.5, 0))
ball = sphere(radius = size, pos=A, color=color.red, make_trail = True, trail_radius = 1)
x_plane = box(length=100, height=0.3, width=5, color=color.blue, pos=vec(30*pi/2,0,0))
y_plane = box(length=0.3, height=65, width=5, color=color.blue, pos=vec(0,30,0))
a_x = graph(width=400, align='left', xtitle='x', ytitle='a', background=vec(1, 1, 1))
c_a_x = gcurve(color=color.cyan, graph=a_x)
a_t = graph(width=400, align='left', xtitle='t', ytitle='a', background=vec(1, 1, 1))
c_a_t = gcurve(color=color.cyan, graph=a_t)
ball.v=vec(0,0,0)

sin=h/sqrt(h**2+d**2)
cos=d/sqrt(h**2+d**2)

t=0
dt=0.0001
while True:
    rate(2000)
    ball.a=vec(g*sin*cos,-g*sin**2,0)
    ball.v+=ball.a*dt
    ball.pos+=ball.v*dt
    t+=dt
    c_a_x.plot(pos=(ball.pos.x,mag(ball.a)))
    c_a_t.plot(pos=(t,mag(ball.a)))
    if ball.pos.y<=0:
        break

print(t)

