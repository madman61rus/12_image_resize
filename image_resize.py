import argparse

def resize_image(path_to_original, path_to_result):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, help="path to original image")
    parser.add_argument("-w","--width", help="width of a new image")
    parser.add_argument("-e","--height", help="height of a new image")
    parser.add_argument("-s", "--scale", help="scale to a new image")
    args = parser.parse_args()
