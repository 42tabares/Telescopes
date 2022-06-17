from vpython import *
from math import radians
import time

checkaxis = True

if checkaxis == True :
    X = arrow(axis=vec(30,0,0), color=color.green, shaftwidth=0.1)
    Y = arrow(axis=vec(0,30,0), color=color.blue, shaftwidth=0.1)
    Z = arrow(axis=vec(0,0,30), color=color.red, shaftwidth=0.1)
    
#Telescope set-up

tube1 = cylinder(pos=vec(0,0,0), radius=2, axis=vec(5,0,0))
tube2 = cylinder(pos=vec(0,0,0), radius=2, axis=vec(-5,0,0))
tube3 = cylinder(pos=vec(-5,0,0), radius=1, axis=vec(-2,0,0))

Telescope = compound([tube1,tube2,tube3])
Telescope.pos = vec(0,0,0)
Telescope.texture = textures.metal

# Axis set up

Dec_Axis = cylinder(pos=vec(0,0,0), radius=1, axis=vec(0,-6,0), color=color.blue)
Ra_Axis = cylinder(pos=vec(0,-4,0), radius=1, axis=vec(-6,0,0), color=color.red)

#Tripod setup, this is only cosmetic

tube2 = cylinder(pos=vec(0,-4,0), radius=3, axis=vec(0,-1,0))
tube3 = cylinder(pos=vec(0,-4,-1), axis=vec(0,0,2))
leg1 = cylinder(pos=vec(0,-5,0), axis=vec(0,-10,0), radius=0.5)
leg1.rotate(angle=radians(30), axis=vec(0,0,1))
leg2 = leg1.clone()
leg2.rotate(angle=radians(120), axis=vec(0,1,0))
leg3 = leg2.clone()
leg3.rotate(angle=radians(120), axis=vec(0,1,0))
Tripod = compound([tube2,tube3,leg1,leg2,leg3])
#Tripod.pos = vec(-5,-10,0)



# .... LATITUDE

Lat = 30 #Change this value to modify the height of the celestial north pole

Ra_Axis.rotate(angle = radians(Lat), axis=vec(0,0,1))
Dec_Axis.rotate(angle = radians(Lat), axis=vec(0,0,1), origin=(Ra_Axis.pos))
Telescope.rotate(angle = radians(Lat), axis=vec(0,0,1), origin=(Ra_Axis.pos))

# .... UI

def RA(x):
    RA_text.text = RA_s.value
def DEC(x):
    DEC_text.text = DEC_s.value
    
scene.append_to_caption('\n\n')
    
wtext(text="Right Acension Axis")
RA_s = slider(min=0, max=359, value=0, step=1, bind=RA, right=15)
RA_text = wtext(text=RA_s.value)

scene.append_to_caption('\n\n\n\n')

wtext(text="Declination Axis")
DEC_s = slider(min=-90, max=90, value=0, step=1, bind=DEC, right=15)
DEC_text = wtext(text=DEC_s.value)

# ..... Simulation

RA_current = RA_s.value
DEC_current = DEC_s.value

while True:
    
    time.sleep(0.001)
    if RA_current != RA_s.value:
        Telescope.rotate(angle= radians(RA_current - RA_s.value), axis=Ra_Axis.axis, origin=(Ra_Axis.pos))
        Dec_Axis.rotate(angle= radians(RA_current - RA_s.value), axis=Ra_Axis.axis, origin=(Ra_Axis.pos))
    if DEC_current != DEC_s.value:
        Telescope.rotate(angle= radians(DEC_s.value - DEC_current), axis=Dec_Axis.axis, origin=(Dec_Axis.pos))    
          
    RA_current = RA_s.value
    DEC_current = DEC_s.value