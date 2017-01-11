import argparse
import os
from PIL import Image

def create_output_name(path_to_original,width,height):
    path, filename = os.path.split(path_to_original)
    splited_filename = filename.split('.')
    new_file_name = '{}__{}x{}.{}'.format(''.join(splited_filename[:-1]),width,height,splited_filename[-1])
    return new_file_name

def resize_image(path_to_original,file_to_output, width=0,height=0,scale=0):
    image = Image.open(path_to_original)
    print(image.format)
    if width and not height and not scale:
        ratio = (int(width) / float(image.size[0]))
        height = int(float(image.size[1]) * ratio)
        size = (int(width),height)
        resized_image = image.resize(size, Image.ANTIALIAS)
        return resized_image

    if height and not width and not scale:
        ratio = (int(height) / float(image.size[1]))
        width = int(float(image.size[0]) * ratio)
        size = (width,int(height))
        resized_image = image.resize(size, Image.ANTIALIAS)
        return resized_image

    if width and height:
        size = int(width),int(height)
        resized_image = image.resize(size,Image.ANTIALIAS)
        return image

def save_resized_image(output,path_to_result,format='JPEG'):
        output.save(path_to_result,format)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, help="Исходное изображение")
    parser.add_argument("-o", "--output", help="Получившееся изображение")
    parser.add_argument("-w","--width", help="width of a new image")
    parser.add_argument("-e","--height", help="height of a new image")
    parser.add_argument("-s", "--scale", help="scale to a new image")
    args = parser.parse_args()

    if args.file :
        image = resize_image(args.file,args.output,width=args.width,height=args.height,scale=args.scale)
        if args.output:
            save_resized_image(image,args.output,format=image.format)
        else:
            save_resized_image(image, args.output, format=image.format)