import stepic
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

img = Image.open('upz.png')
data = stepic.decode(img)
print(data)