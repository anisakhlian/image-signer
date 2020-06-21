import os
import argparse
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def sign_images(output_dir=None):
    source_dir = 'source-images'
    font = ImageFont.truetype('arial.ttf', 30)
    if not output_dir:
        output_dir = 'output-images'

    for filename in os.listdir(source_dir):
        title = ' '.join(filename.split('.')[0].split('-')).title()
        sign = ''.join((u'\u00A9', title))

        path = os.path.join(source_dir, filename)
        img = Image.open(path)
        width, height = img.size
        
        draw = ImageDraw.Draw(img)
        draw.text((width-50-len(title)*15, height-50), sign, font=font)

        if not os.path.isdir(output_dir):
            os.mkdir(output_dir)
        img.save(os.path.join(output_dir, filename))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-d', '--directory', required=False, help='directory for output images')
    args = vars(ap.parse_args())
    sign_images(args.get('directory', None))

