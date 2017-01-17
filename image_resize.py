import argparse
import os
from PIL import Image


def create_output_name(path_to_original, size):
    path, filename = os.path.split(path_to_original)
    splited_filename = filename.split('.')
    new_file_name = '{}_{}x{}.{}'.format(''.join(splited_filename[:-1]), size[0], size[1], splited_filename[-1])
    return os.path.join(os.path.dirname(args.file), new_file_name)


def calculate_height(width, image_width):
    ratio = (int(width) / float(image_width))
    height = int(float(image.size[1]) * ratio)
    size = int(width), height
    return size


def calculate_width(height, image_height):
    ratio = (int(height) / float(image_height))
    width = int(float(image.size[0]) * ratio)
    size = width, int(height)
    return size


def calculate_scaled_width(scale, size):
    size = size[0] * scale, size[1] * scale
    return size


def is_image_right_scalled(size_image, size):
    ratio_image = size_image[0] / size_image[1]
    new_size_image = size[0] / size[1]
    if not ratio_image == new_size_image:
        return False
    else:
        return True


def load_original_image(path_to_original):
    try:
        image = Image.open(path_to_original)
        return image
    except IOError:
        return None


def resize_image(image, size):
    new_image = image.resize(size, Image.ANTIALIAS)
    return new_image


def save_resized_image(resized_image, path_to_result, format='JPEG'):
    resized_image.save(path_to_result, format)


def print_error_scale(width, height):
    print('Пропорции не совпадают ')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, help="Исходное изображение")
    parser.add_argument("-o", "--output", help="Получившееся изображение")
    parser.add_argument("-w", "--width", help="width of a new image")
    parser.add_argument("-e", "--height", help="height of a new image")
    parser.add_argument("-s", "--scale", help="scale to a new image")
    args = parser.parse_args()

    if args.width and args.height and args.scale:
        print('Нельзя передавать вместе и размеры и масштаб')
    else:
        image = load_original_image(args.file)
        size = image.size

        if args.width and not args.height:
            size = calculate_height(args.width, size[0])
        if not args.width and args.height:
            size = calculate_width(args.height, size[1])
        if args.scale and not args.width and not args.height:
            size = calculate_scaled_width(int(args.scale), image.size)
        else:
            size = int(args.width), int(args.height)
            if not is_image_right_scalled(image.size, size):
                print('Внимание ! Пропорции не совпадают с исходным изображением')

        resized_image = resize_image(image, size)

        if args.output:
            output_path = args.output
        else:
            output_path = create_output_name(args.file, size)

        try:
            save_resized_image(resized_image, output_path)
        except IOError:
            print('Ошибка при сохранении файла')
