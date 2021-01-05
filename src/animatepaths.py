import svgpathtools as svg
from svgpathtools import kinks, smoothed_path
import copy
from svgpathtools import disvg
from svgpathtools import parse_path, Line, Path, wsvg


paths, attributes = svg.svg2paths('pathsvg/7hours.svg')

path = paths[0]

cp = copy.deepcopy(path)
# print(path)

cont = path.continuous_subpaths()

smoothed =[]
help(smoothed_path)

s = path
for i,u in enumerate(s[:-1]):
    
    
        # print(u.end)
    l =Line(s[i].end,s[i+1].end)
    print(l)
    smoothed.append(l)
    # ss.insert(3,l)
    # print("smoothed", smoothed_path(cont[i]))  
    # print(l) 
    # smoothed.append(segm)
# print(len(cont))

# del smoothed[2]
# from time import sleep
disvg(smoothed)
# help(disvg)
# sleep(1)  # needed when not giving the SVGs unique names (or not using timestamp)

# print("Notice that path contains {} segments and spath contains {} segments."
      # "".format(len(path), len(spath)))