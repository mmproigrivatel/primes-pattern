from PIL import Image, ImageDraw

def is_prime(a):
    r = False
    for i in range(2, a//2):
        if a%i==0: r = True
    return r

img = Image.new('RGB', (100, 100))
imgDraw = ImageDraw.Draw(img)
pix = img.load()

for x in range(img.size[0]):
    for y in range(img.size[1]):
        if not is_prime(x^y):
            imgDraw.point((x, y), (0, 0, 255))

img.save('xor.png')
