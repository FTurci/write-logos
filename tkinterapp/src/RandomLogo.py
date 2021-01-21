
# Import the required packages: 
from bs4 import BeautifulSoup
import requests
import re 
import tkinter 
from tkinter.filedialog import asksaveasfile
from PIL import ImageTk,Image
import tempfile
import random
import urllib


def get_urls():
    # Store the url as a string scalar: url => str
    url = 'https://github.com/FTurci/write-logos/tree/main/src/pngs'

    # Issue request: r => requests.models.Response
    r = requests.get(url)

    # Extract text: html_doc => str
    html_doc = r.text

    # Parse the HTML: soup => bs4.BeautifulSoup
    soup = BeautifulSoup(html_doc)

    # Find all 'a' tags (which define hyperlinks): a_tags => bs4.element.ResultSet
    a_tags = soup.find_all('a')

    # Store a list of urls ending in .csv: urls => list
    urls = ['https://raw.githubusercontent.com'+re.sub('/blob', '', link.get('href')) 
            for link in a_tags  if '.png' in link.get('href')]
    return urls



window = tkinter.Tk()  
# top = tkinter.Frame()
# top.pack(side="top")
label = tkinter.Label(window)
#The Pack geometry manager packs widgets in rows or columns.
label.pack(side = "top", fill = "both", expand = "yes")   
statusbar = tkinter.Label(window)



urls = get_urls()
path = '/Users/francesco/Pictures/me.JPG'          
print(urls)

which = random.randint(0, len(urls))
# fname = 'temp-logo-extemporanea.png'

url = urls[which]
r = requests.get(url)
tmpfile = tempfile.NamedTemporaryFile()
tmpfile.write(r.content)
 

print(tmpfile.name)



window.title("Logo Casuale eXtemporanea")
window.geometry("800x400")
window.configure()#background='grey')


img = ImageTk.PhotoImage(Image.open(tmpfile.name))
label.config(image=img)
statusbar.configure(text=urllib.parse.unquote(urls[which].split('pngs/')[1]),relief=tkinter.SUNKEN, anchor=tkinter.W)

def saveCallback():
    file = asksaveasfile(mode='w', defaultextension=".png")
    print(dir(file))
    print(file)
    if file:
        im = Image.open(tmpfile.name)
        im.save(file.name) # saves the image to the input file name.

def shuffleCallback():
    which = random.randint(0, len(urls))
    tmp = tempfile.NamedTemporaryFile()
    r = requests.get(urls[which])
    tmp.write(r.content)
    img2 = ImageTk.PhotoImage(Image.open(tmp.name))
    label.configure(image=img2)
    label.image = img2
    statusbar.configure(text=urllib.parse.unquote(urls[which].split('pngs/')[1]),relief=tkinter.SUNKEN,anchor=tkinter.W)

    # window.update_idletasks()
    print(tmp.name)

quit = tkinter.Button(window, text="Esci", command=window.destroy) 
quit.pack(side="right") 

shuffle = tkinter.Button(window, text ="Rimescola", command = shuffleCallback)
save = tkinter.Button(window, text ="Salva", command = saveCallback)
save.pack(side="right")

shuffle.pack(side="right")

statusbar.pack(#side="left",
 fill=tkinter.X)

tkinter.mainloop()         




