from PIL import Image
import PIL.ImageOps
from io import BytesIO


def InvertImage(file):
    img = Image.open(file)
    img_inverted = PIL.ImageOps.invert(img)
    output = BytesIO()
    img_inverted.save(output, 'JPEG')
    output.seek(0)
    return output

