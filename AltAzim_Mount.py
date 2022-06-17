from vpython import *
from math import radians
import time

checkaxis = True

if checkaxis == True :
    X = arrow(axis=vec(30,0,0), color=color.green, shaftwidth=0.1)
    Y = arrow(axis=vec(0,30,0), color=color.blue, shaftwidth=0.1)
    Z = arrow(axis=vec(0,0,30), color=color.red, shaftwidth=0.1)

# .... Telescope

tube1 = cylinder(pos=vec(0,0,0), radius=2, axis=vec(5,0,0))
tube2 = cylinder(pos=vec(0,0,0), radius=2, axis=vec(-5,0,0))
tube3 = cylinder(pos=vec(-5,0,0), radius=1, axis=vec(-2,0,0))

Telescope = compound([tube1,tube2,tube3])
Telescope.pos = vec(0,0,0)
Telescope.texture = textures.metal

# .... Mount

tube1 = cylinder(pos=vec(0,0,-3), radius=1, axis=vec(0,0,6))
box1 = box(pos=vec(0,-2,-2), size=vec(1,-4,1))
box2 = box(pos=vec(0,-2,2), size=vec(1,-4,1))

Mount = compound([tube1,box1,box2])

#Tripod setup, this is only cosmetic

tube2 = cylinder(pos=vec(0,-4,0), radius=3, axis=vec(0,-1,0))
leg1 = cylinder(pos=vec(0,-5,0), axis=vec(0,-10,0), radius=0.5)
leg1.rotate(angle=radians(30), axis=vec(0,0,1))
leg2 = leg1.clone()
leg2.rotate(angle=radians(120), axis=vec(0,1,0))
leg3 = leg2.clone()
leg3.rotate(angle=radians(120), axis=vec(0,1,0))

# .... UI

def AZ(x):
    AZ_text.text = AZ_s.value
def H(x):
    H_text.text = H_s.value
    
scene.append_to_caption('\n\n')
    
wtext(text="Azimuth")
AZ_s = slider(min=0, max=359, value=0, step=1, bind=AZ, right=15)
AZ_text = wtext(text=AZ_s.value)

scene.append_to_caption('\n\n\n\n')

wtext(text="Height")
H_s = slider(min=0, max=80, value=0, step=1, bind=H, right=15)
H_text = wtext(text=H_s.value)

# ..... Simulation

AZ_current = AZ_s.value
H_current = H_s.value

while True:
    
    time.sleep(0.001)
    if AZ_current != AZ_s.value:
        Telescope.rotate(angle= radians(AZ_current - AZ_s.value), axis=vec(0,1,0))
        Mount.rotate(angle= radians(AZ_current - AZ_s.value), axis=vec(0,1,0))
    if H_current != H_s.value:
        Telescope.rotate(angle= radians(H_s.value - H_current), axis=cross(Telescope.axis,vec(0,1,0)))    
          
    AZ_current = AZ_s.value
    H_current = H_s.value
        

