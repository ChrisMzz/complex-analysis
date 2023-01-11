from PIL import Image

gif = []
files = []
for n in range(0,128):
    files.append(f"dump/cot/{n}.png")


# using https://stackoverflow.com/a/451580/17091581
# rescale
rescale = False
if rescale:
    basewidth = 1200
    for f in files:
        picture = Image.open(f)
        wpercent = (basewidth/float(picture.size[0]))
        hsize = int((float(picture.size[1])*float(wpercent)))
        picture = picture.resize((basewidth,hsize), Image.Resampling.LANCZOS)
        gif.append(picture)
else:
    for f in files:
        gif.append(Image.open(f))

gif[0].save('betterztoc.gif', save_all=True, optimize=False, append_images=gif[1:], loop=0, )
