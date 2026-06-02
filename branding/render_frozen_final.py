# -*- coding: utf-8 -*-
"""Frozen World icon: pale sky + snow + ice spikes (ice_spikes spires). Style matches sky/mountain."""
import os
from PIL import Image, ImageDraw
SS=4; MASTER=512; N=MASTER*SS
HERE=os.path.dirname(__file__); RES=os.path.abspath(os.path.join(HERE,"..","src","main","resources"))
SKY=(198,216,232); SNOW=(243,247,251); SNOW_DK=(214,226,240); ICE=(176,214,234); ICE_DK=(140,188,218)
def spike(d,cx,base,w,h):
    d.polygon([(cx-w/2,base),(cx+w/2,base),(cx+w*0.06,base-h)],fill=ICE)
    d.polygon([(cx+w*0.06,base-h),(cx+w/2,base),(cx+w*0.18,base)],fill=ICE_DK)
    d.polygon([(cx-w/2,base),(cx+w*0.06,base-h),(cx-w*0.10,base)],fill=SNOW)
def render():
    img=Image.new("RGB",(N,N),SKY); d=ImageDraw.Draw(img)
    base=int(N*0.82)
    spike(d,int(N*0.24),base,int(N*0.22),int(N*0.46))
    spike(d,int(N*0.78),base,int(N*0.24),int(N*0.52))
    spike(d,int(N*0.50),base,int(N*0.30),int(N*0.70))
    d.rectangle([0,base,N,N],fill=SNOW)             # snow ground
    for bx in range(0,N+1,int(N*0.26)):             # gentle snow drifts
        r=int(N*0.13); d.ellipse([bx-r,base-r*0.4,bx+r,base+r],fill=SNOW_DK); d.ellipse([bx-r,base-r*0.4,bx+r,base+r*0.4],fill=SNOW)
    return img
m=render().resize((MASTER,MASTER),Image.LANCZOS)
m.save(os.path.join(HERE,"frozen_world_icon_512.png"))
for sz in (256,128,64): m.resize((sz,sz),Image.LANCZOS).save(os.path.join(HERE,f"frozen_world_icon_{sz}.png"))
os.makedirs(RES,exist_ok=True); m.resize((256,256),Image.LANCZOS).save(os.path.join(RES,"frozen_world.png"))
print("frozen icon written")
