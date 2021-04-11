#!/usr/bin/env python3
from image import *

def greyPixel(p):
    # returns a gray pixel, the gray value is calculated by adding the RGB value and 
    # dividing the sum by three 
    average = (p.getRed() + p.getGreen() + p.getBlue()) // 3
    return Pixel(average, average, average)

def gray_scale(img):
    # assigns the image object to a variable, configures the window object and draws it to the screen 
    old_image = Image(img)
    image_window = ImageWin(old_image.getWidth(), old_image.getHeight(), "Boat")
    old_image.draw(image_window)
    print('click image to close')
    
    # creates some width and height variables based on the old images dimensions
    width = old_image.getWidth()
    height = old_image.getHeight()
    new_jpg = EmptyImage(width, height)

    # double loop to assign every pixel a gray value
    for row in range(height):
        for col in range(width):
            original_pixel = old_image.getPixel(col, row)
            new_pixel = greyPixel(original_pixel)
            new_jpg.setPixel(col, row, new_pixel)
    
    # seup the newly generated graphic into the canvas
    new_jpg.setPosition(width+1, 0)
    new_jpg.draw(image_window)

    # save the new graphic
    new_jpg.save('boat-bw.png')

    # click to exit
    image_window.exitOnClick()
    print('conversion complete')

def main():
    jpg_file = gray_scale("boat-small.jpg")

if __name__ == "__main__":
    main()