#!C:\Users\alshe\AppData\Local\Programs\Python\Python39\python.exe
print("Content-type: text/html\n\n")
print()
print("<html><head>")
print("")
print("</head><body>")
text = "Романова"
from PIL import Image, ImageDraw, ImageFont
import numpy as np
myfont = ImageFont.truetype("verdanab.ttf", 12)
size = myfont.getsize(text)
img = Image.new("1",size,"black")
draw = ImageDraw.Draw(img)
draw.text((0, 0), text, "white", font=myfont)
pixels = np.array(img, dtype=np.uint8)
chars = np.array([' ','#'], dtype="U1")[pixels]
strings = chars.view('U' + str(chars.shape[1])).flatten()
print('<pre>')
for i in strings:
    print(i)
print("</pre></body></html>")
