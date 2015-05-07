from PIL import Image, ImageDraw

def stamp(file):
    im = Image.open(file)
    draw = ImageDraw.Draw(im)
    draw.ellipse((370, 237, 374, 241), fill=255)
    del draw
    return im.save("P_" + file)

for hh in range(10, 17):
    for mm in range(0, 6):
        time_stamp = (str(hh).rjust(2, "0") + str(mm).ljust(2, "0"))
        stemp(date + time_stamp + ".gif")
