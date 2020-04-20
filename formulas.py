#!/usr/bin/env python3

from config_file import *
import math

# 2 dimensional shapes

def tri_a(b,h):
    return (b*h)/2

def circ_c(r):
    return (r*2)*pi

def circ_a(r):
    return (r*r)*pi

def re_a(l,w):
    return l*w

def sq(s):
    return s*s

# 3 dimensional shapes

def cy_sa(r,h):
    return (circ_a(r)*2) + (circ_c(r)*h)

def rcy_sa(m,x,a):
    if m.lower() == "r":
        return "N/A"
    elif m.lower() == "h":
        return (a-(circ_a(x)*2))/circ_c(x)

def cy_v(r,h):
    return circ_a(r)*h

def itri_sa(x,y,z,s):
    return (tri_a(x,y)*2) + (re_a(s,z)*2) + re_a(x,z)

def itri_v(w,l,h):
    return 0.5*w*l*h

def ritri_v(v,g1,g2):
    return (v/g1)/g2/0.5

def rect_sa(x,y,z):
    return ((x*y)*2) + ((x*z)*2) + ((y*z)*2)

def rrect_sa(a,g1,g2):
    return (a-(2*(g1*g2)))/((g1*2)+(g2*2))

def rect_v(x,y,z):
    return x*y*z

def rrect_v(a,g1,g2):
    return (a/g1)/g2

def rcub_sa(a):
    return math.sqrt(a/6)

def rcub_v(a):
    return math.pow(a,1/3)

def con_sa(r,s):
    return circ_a(r) + (pi*r*s)

def sqpy_sa(b,h):
    return (b*b) + (4*tri_a(b,h))

def itrip_sa(bl,bh,s):
    return tri_a(bl,bh) + (3*tri_a(bl,s))

def sph_sa(r):
    return 4*pi*(r*r)

def sph_v(r):
    return (4/3)*pi*(r*r*r)

def sph_sav(sa):
    return sph_v(math.sqrt(sa/(pi*4)))

def sph_vsa(v):
    return sph_sa(math.pow(v/(pi*4/3),1/3))

def hsph_sa(r):
    return 3*pi*(r*r)

def hsph_v(r):
    return (2/3)*pi*(r*r*r)

def con_v(r,h):
    return (1/3)*pi*(r*r)*h

def tripy_v(w,l,h):
    return (1/3)*w*l*h

def sqpy_v(b,h):
    return (1/3)*(b*b)*h

def repy_v(b1,b2,h):
    return (1/3)*(b1*b2)*h

# misc

def sa_simsols(n,r1,r2):
    return math.pow(r1/r2,3)*n

def tri_sa_simsols(o,r1,r2):
    return math.pow(r2/r1,2)*o

def get_vss_ratio(r1,r2):
    #return math.pow(r1/r2,3)
    return str(math.pow(r1,3))+":"+str(math.pow(r2,3))

def get_sass_ratio(r1,r2):
    #return math.pow(r1/r2,2)
    return str(math.pow(r1,2))+":"+str(math.pow(r2,2))
