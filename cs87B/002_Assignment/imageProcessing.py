#!/usr/bin/env python3.9
from image import *

def greyPixel(p):
    average = (p.getRed() + p.getGreen() + p.getBlue()) // 3
    return Pixel(average, average, average)

def gray_scale(img):
    old_image = Image(img)
    image_window = ImageWin(old_image.getWidth(), old_image.getHeight(), "Boat")
    old_image.draw(image_window)

    width = old_image.getWidth()
    height = old_image.getHeight()
    new_jpg = EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            original_pixel = old_image.getPixel(col, row)
            new_pixel = greyPixel(original_pixel)
            new_jpg.setPixel(col, row, new_pixel)
    
    new_jpg.setPosition(width+1, 0)
    new_jpg.draw(image_window)
    new_jpg.save('boat-bw.png')
    image_window.exitOnClick()
    print('conversion complete')

def main():
    jpg_file = gray_scale("boat-small.jpg")

if __name__ == "__main__":
    main()