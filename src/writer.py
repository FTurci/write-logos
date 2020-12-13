import svgwrite as svg

# check this to change fonts https://stackoverflow.com/questions/17127083/python-svgwrite-and-font-styles-sizes


width = 500
height = 200

dwg = svg.Drawing(filename="in.svg", size=(f"{width}px", f"{height}px"))

# g = dwg.g(style="font-size:30;font-family:Zapfino;font-weight:bold;font-style:oblique;stroke:black;stroke-width:1;fill:none")

# dwg.defs.add(dwg.style(' @import url("https://fonts.googleapis.com/css?family=Pacifico:400,400i,700,700i");'))
dwg.defs.add(
    dwg.style(
        """    
 @font-face {font-family:Scriptina;
 src: url('fonts/SCRIPTIN.ttf');}"""
    )
)
g = dwg.g(style="font-size:30;font-family:Scriptina;")
g.add(dwg.text("eXtemporanea", insert=(width * 0.4, height * 0.4)))
# settings are valid for all text added to 'g'
dwg.add(g)
dwg.save()

print(dwg.tostring())
# trick to convert the svg with fonts to a path

import subprocess

subprocess.call(
    "inkscape in.svg --export-text-to-path --export-plain-svg -o out.svg", shell=True
)
