from PIL import Image, ImageFont,ImageDraw



data=Image.open("/home/gowtham/Pictures/img.jpg")
print(data.size,data.format)
data.show()

img_width,img_height=data.size
draw=ImageDraw.Draw(data)
text="this is a demo"

draw.setfont("arial.ttf",12)
textwidth,textheight=draw.textsize(text)

margin=5
x=img_width-textwidth-margin
y=img_height-textheight-margin

draw.text((x,y),text)
data.save("/home/gowtham/Pictures/img_cpy.jpeg")

