# @Francesco_Turci

import svgwrite as svg
import glob
import subprocess
import io
import itertools
import os
import pathlib
import numpy as np
# check this to change fonts https://stackoverflow.com/questions/17127083/python-svgwrite-and-font-styles-sizes

def parse_info(info):
    buf = io.StringIO(info)
    information = {}
    for l in buf:
        try:
            split = l.split(":")
            # print(split)
            key = split[0]
            value = split[1].strip()
            information[key]=value
        except:
            pass
    return information


def print_logo(fontpath1, fontpath2,fontsize=30, width = 500, height = 200): 
    
    print("p1", fontpath1,pathlib.PurePosixPath(fontpath1))
    fontpath1 = pathlib.Path(pathlib.PurePosixPath(fontpath1)).resolve()
    fontpath2 = pathlib.Path(pathlib.Path(fontpath2)).resolve()
    print (fontpath1)
    print (fontpath2)  

    fontname1 = os.path.basename(fontpath1).split('.ttf')[0]
    fontname2 = os.path.basename(fontpath2).split('.ttf')[0]
    if os.path.exists(f"pngs/{fontname1}+{fontname2}.png"):
        print(f"Image pngs/{fontname1}+{fontname2}.png already exists. Skipping...")
        return -1
    # get the info on the font
    otfinfo1 = subprocess.check_output(f'otfinfo --info "{fontpath1}"', shell=True).decode("utf-8") 
    otfinfo2 = subprocess.check_output(f'otfinfo --info "{fontpath2}"', shell=True).decode("utf-8") 
    # print(info)
    info1 = parse_info(otfinfo1)
    info2 = parse_info(otfinfo2)
    
    dwg = svg.Drawing(filename=f"textsvg/{fontname1}+{fontname2}.svg", size=(f"{width}px", f"{height}px"))

    # Define style: here we include the pah to the custom font
    dwg.defs.add(
        dwg.style(
            """    
     @font-face {font-family:%s;
     src: url('%s');}
     @font-face {font-family:%s;
     src: url('%s');}
     """%(info1['Family'],fontpath1, info2['Family'], fontpath2)
        )
    )
    # use the style
    g = dwg.g(style=f"font-size:{fontsize};")#font-family:{info1['Family']};")#font-weight:bold;font-style:oblique;stroke:black;stroke-width:1;fill:red")

    atext = dwg.text("", x=["50%"],y=["50%"], text_anchor="middle")
    atext.add(dwg.tspan('E', font_family=info1['Family'],letter_spacing= "0.075em"))
    atext.add(dwg.tspan('X', font_family=info2['Family'],letter_spacing= "0.05em"))
    atext.add(dwg.tspan('TEMPORANEA', font_family=info1['Family'],letter_spacing= "0.075em"))
    g.add(atext)#, x=["50%"],y=["50%"], text_anchor="middle"))
    # settings are valid for all text added to 'g'
    dwg.add(g)
    dwg.save()
    # trick to convert the svg with fonts to a path: using inkscape
    subprocess.call(
        f'inkscape "textsvg/{fontname1}+{fontname2}.svg" --export-text-to-path --export-plain-svg -o "pathsvg/{fontname1}+{fontname2}.svg"', shell=True
    )
    subprocess.call(
        f'inkscape  "pathsvg/{fontname1}+{fontname2}.svg" -o "pngs/{fontname1}+{fontname2}.png"', shell=True
    )
    
    subprocess.call(
        f'convert -flatten  "pngs/{fontname1}+{fontname2}.png" "pngs/{fontname1}+{fontname2}.png"', shell=True
    )


# N = 5
fonts_E_TEMPORANEA = glob.glob("fonts/Fonts_E_TEMPORANEA/*f")#[:N]
fonts_X = glob.glob("fonts/Fonts_X/*f")#[:N]


for x in fonts_X:
    for rest in fonts_E_TEMPORANEA:
        print_logo(rest,x,fontsize=60, width=800)
