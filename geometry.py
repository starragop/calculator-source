#!/usr/bin/env python3
from config_file import *
from formulas import *

def getInput(text):
    return input(text + " >")
def getNumber(text):
    return float(getInput(text))

def dostuff():
    thing = getInput("Operation")
    if thing == "exit":
        exit(0)
    elif thing == "cy_sa":
        print(cy_sa(getNumber("Radius"),getNumber("Height")))
    elif thing == "cy_v":
        print(cy_v(getNumber("Radius"),getNumber("Height")))
    elif thing == "circ_sa":
        print(circ_sa(getNumber("Radius")))
    elif thing == "circ_a":
        print(circ_a(getNumber("Radius")))
    elif thing == "itri_sa":
        print(itri_sa(getNumber("x"),getNumber("y"),getNumber("z"),getNumber("s")))
    elif thing == "rect_sa":
        print(rect_sa(getNumber("x"),getNumber("y"),getNumber("z")))
    elif thing == "rect_v":
        print(rect_v(getNumber("x"),getNumber("y"),getNumber("z")))
    elif thing == "rcy_sa":
        print(rcy_sa(getInput("Missing"),getNumber("Given"),getNumber("Total Surface Area")))
    elif thing == "rrect_sa":
        print(rrect_sa(getNumber("Total Surface Area"),getNumber("Given 1"),getNumber("Given 2")))
    elif thing == "rrect_v":
        print(rrect_v(getNumber("Total Surface Area"),getNumber("Given 1"),getNumber("Given 2")))
    elif thing == "rcub_sa":
        print(rcub_sa(getNumber("Total Surface Area")))
    elif thing == "rcub_v":
        print(rcub_v(getNumber("Total Surface Area")))
    elif thing == "con_sa":
        print(con_sa(getNumber("Radius"),getNumber("Slant Height")))
    elif thing == "sqpy_sa":
        print(sqpy_sa(getNumber("Base"),getNumber("Height")))
    elif thing == "itrip_sa":
        print(itrip_sa(getNumber("Base Length"),getNumber("Base Height"),getNumber("Slant Height")))
    elif thing == "sph_sa":
        print(sph_sa(getNumber("Radius")))
    elif thing == "sph_v":
        print(sph_v(getNumber("Radius")))
    elif thing == "itri_v":
        print(itri_v(getNumber("Width"),getNumber("Length"),getNumber("Height")))
    elif thing == "ritri_v":
        print(ritri_v(getNumber("Volume"),getNumber("Given 1"),getNumber("Given 2")))
    elif thing == "con_v":
        print(con_v(getNumber("Radius"),getNumber("Height")))
    elif thing == "sqpy_v":
        print(sqpy_v(getNumber("Base"),getNumber("Height")))
    elif thing == "repy_v":
        print(repy_v(getNumber("Base 1"),getNumber("Base 2"),getNumber("Height")))
    elif thing == "m":
        print(getNumber("1")*getNumber("2"))
    elif thing == "d":
        print(getNumber("1")/getNumber("2"))
    elif thing == "a":
        print(getNumber("1")+getNumber("2"))
    elif thing == "s":
        print(getNumber("1")-getNumber("2"))
    elif thing == "sa_simsols":
        print(sa_simsols(getNumber("New Value"),getNumber("Before Reference"),getNumber("After Reference")))
    elif thing == "tri_sa_simsols":
        print(tri_sa_simsols(getNumber("Old Value"),getNumber("Before Reference"),getNumber("After Reference")))
    elif thing == "get_vss_ratio":
        print(get_vss_ratio(getNumber("Before"),getNumber("After")))
    elif thing == "get_sass_ratio":
        print(get_sass_ratio(getNumber("Before"),getNumber("After")))
    elif thing == "sph_vsa":
        print(sph_vsa(getNumber("Volume")))
    elif thing == "sph_sav":
        print(sph_sav(getNumber("Total Surface Area")))
    elif thing == "tripy_v":
        print(tripy_v(getNumber("Width"),getNumber("Length"),getNumber("Height")))


while True:
    dostuff()
