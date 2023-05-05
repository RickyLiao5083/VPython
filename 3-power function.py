#f(x)=60/(-30pi)^3*(x-30pi)^3
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

def f(x):
    return 60/(-30*pi)**3*(x-30*pi)**3

i,n,t=0,942478,0
while True:
    rate(100000)
    i+=1
    x1=30*pi/n*i
    y1=f(x1)
    x2=30*pi/n*(i+1)
    y2=f(x2)
    ball.pos.x=x2
    ball.pos.y=y2
    s=sqrt((x2-x1)**2+(y2-y1)**2)
    v1=sqrt(abs(2*g*(h-y1)))
    a_t=(y1-y2)/s*g
    v2=sqrt(abs(v1**2+2*a_t*s))
    t12=(v2-v1)/a_t
    t+=t12
    c_a_x.plot(pos=(x1,a_t))
    c_a_t.plot(pos=(t,a_t))
    if i==n:
        break

print(t)

