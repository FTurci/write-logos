import svgwrite as svg

# check this to change fonts https://stackoverflow.com/questions/17127083/python-svgwrite-and-font-styles-sizes


width = 500
height = 200

dwg = svg.Drawing(filename="in.svg", size=(f"{width}px", f"{height}px"))

# Define style: here we include the pah to the custom font
dwg.defs.add(
    dwg.style(
        """    
 @font-face {font-family:Scriptina;
 src: url('fonts/SCRIPTIN.ttf');}"""
    )
)
# use the style
g = dwg.g(style="font-size:30;font-family:Scriptina;font-weight:bold;font-style:oblique;stroke:black;stroke-width:1;fill:red")
g.add(dwg.text("eXtemporanea", insert=(width * 0.4, height * 0.4)))
# settings are valid for all text added to 'g'
dwg.add(g)
dwg.save()
# trick to convert the svg with fonts to a path: usingh inkscape
import subprocess
subprocess.call(
    "inkscape in.svg --export-text-to-path --export-plain-svg -o out.svg", shell=True
)
