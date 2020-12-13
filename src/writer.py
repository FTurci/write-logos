import svgwrite as svg
import glob
import subprocess
import io
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

def print_logo(fontname, width = 500,height = 200, fontpath="/Users/francesco/Repos/write-logos/src/fonts/"):     

    # get the info on the font
    otfinfo = subprocess.check_output(f'otfinfo --info {fontpath}/{fontname}.ttf', shell=True).decode("utf-8") 
    # print(info)
    info = parse_info(otfinfo)
    
    dwg = svg.Drawing(filename=f"textsvg/{fontname}.svg", size=(f"{width}px", f"{height}px"))

    # Define style: here we include the pah to the custom font
    dwg.defs.add(
        dwg.style(
            """    
     @font-face {font-family:%s;
     src: url('%s/%s.ttf');}"""%(info['Family'],fontpath,fontname)
        )
    )
    # use the style
    g = dwg.g(style=f"font-size:30;font-family:{info['Family']};")#font-weight:bold;font-style:oblique;stroke:black;stroke-width:1;fill:red")
    g.add(dwg.text("eXtemporanea", dx=[100],dy=[100]))
    # settings are valid for all text added to 'g'
    dwg.add(g)
    dwg.save()
    # trick to convert the svg with fonts to a path: usingh inkscape
    subprocess.call(
        f"inkscape textsvg/{fontname}.svg --export-text-to-path --export-plain-svg -o pathsvg/{fontname}.svg", shell=True
    )
fonts = glob.glob("fonts/*")
fonts = [f.split('.ttf')[0].split('/')[1] for f in fonts]

for f in fonts:
    print(f)
    print_logo(f)