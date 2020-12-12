import svgwrite as svg

# check this to change fonts


width = 300
height= 200

dwg = svg.Drawing(filename = "test-svgwrite.svg",
                                size = (f"{width}px", f"{height}px"))

dwg.add_stylesheet("style.css", title="") # same rules as for html files

g = dwg.g(class_="mystyle")
g.add(dwg.text("eXtemporanea", insert=(width*0.4, height*0.4))) # settings are valid for all text added to 'g'
dwg.add(g)
dwg.save()