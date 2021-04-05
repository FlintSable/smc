# import image

# win = image.ImageWin(480, 640, "Image Processing")
# original_image = image.FileImage('boat-small.jpg')

# width = original_image.get_width()
# height = original_image.get_height()
# print(width, height)

# original_image.draw(win)
# my_image = original_image.copy()

# for row in range(height):
#     for col in range(width):
#          v = my_image.get_pixel(col,row)
#          v.red = 255 - v.red
#          v.green = 255 - v.green
#          v.blue = 255 - v.blue
#          my_image.set_pixel(col,row,v)

# my_image.draw(win)
# print(win.get_mouse())
# my_image.save('lcastle-inverted.jpg')
# print(my_image.to_list())
# win.exit_on_click()

from image import *

def grayPixel(p):
    avg = (p.getRed() + p.getGreen() + p.getBlue()) // 3
    return Pixel(avg,avg,avg)

def makeGrayScale(imageFile):
    myimagewindow = ImageWin(600,200, "Image Processing")
    oldimage = Image(imageFile)
    oldimage.draw(myimagewindow)

    width = oldimage.getWidth()
    height = oldimage.getHeight()
    newim = EmptyImage(width,height)

    for row in range(height):
        for col in range(width):
            originalPixel = oldimage.getPixel(col,row)
            newPixel = grayPixel(originalPixel)
            newim.setPixel(col,row,newPixel)

    newim.setPosition(width+1,0)
    newim.draw(myimagewindow)
    newim.save('boat-bw.jpg')
    myimagewindow.exitOnClick()



makeGrayScale('boat-small.jpg')