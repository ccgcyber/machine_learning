#coding:utf-8
import sys,os
from PIL import Image,ImageDraw

#Binary array
t2val = {}
def twoValue(image,G):
    for y in xrange(0,image.size[1]):
        for x in xrange(0,image.size[0]):
            g = image.getpixel((x,y))
            if g > G:
                t2val[(x,y)] = 1
            else:
                t2val[(x,y)] = 0

# Noise reduction
# According to the RGB value of a point A, a value N (0 <N <8) is set to be compared with the RBG value of the surrounding 8 points. When the RGB value of A is less than N with the RGB of the surrounding 8 points, This point for the noise
# G: Integer Image binarization threshold
# N: Integer Noise reduction rate 0 <N <8
# Z: Integer Number of noise reductions
# Output
#  0：Noise reduction success
#  1：Noise reduction failed
def clearNoise(image,N,Z):

    for i in xrange(0,Z):
        t2val[(0,0)] = 1
        t2val[(image.size[0] - 1,image.size[1] - 1)] = 1
        print image.size[0]#宽
        print image.size[1]#高
        for x in xrange(1,image.size[0] - 1 ):
            for y in xrange(1,image.size[1] - 1):

                nearDots = 0
                L = t2val[(x,y)]
                if L == t2val[(x - 1,y - 1)]:
                    nearDots += 1
                if L == t2val[(x - 1,y)]:
                    nearDots += 1
                if L == t2val[(x- 1,y + 1)]:
                    nearDots += 1
                if L == t2val[(x,y - 1)]:
                    nearDots += 1
                if L == t2val[(x,y + 1)]:
                    nearDots += 1
                if L == t2val[(x + 1,y - 1)]:
                    nearDots += 1
                if L == t2val[(x + 1,y)]:
                    nearDots += 1
                if L == t2val[(x + 1,y + 1)]:
                    nearDots += 1

                if nearDots < N:
                    t2val[(x,y)] = 1

def pIx(self):
    data = self
    #Picture length and width
    w = self.size[1]
    h = self.size[0]

    #data.getpixel((x,y)) Gets the target pixel color。
    #data.putpixel((x,y),255) Change the pixel color，255 On behalf of color。

    try:
        for x in xrange(1,w-1):
            if x > 1 and x != w-2:
                #Gets the target pixel left and right position
                left = x - 1
                right = x + 1

            for y in xrange(1,h-1):
                # Get the target pixel up and down position
                up = y - 1
                down = y + 1

                if x <= 2 or x >= (w - 2):
                    data.putpixel((x,y),255)

                elif y <= 2 or y >= (h - 2):
                    data.putpixel((x,y),255)

                elif data.getpixel((x,y)) == 0:
                    if y > 1 and y != h-1:

                        # Target the pixel point as the center point，Gets the surrounding pixel color
                        # 0 is black，255 Is white
                        up_color = data.getpixel((x,up))
                        down_color = data.getpixel((x,down))
                        left_color = data.getpixel((left,y))
                        left_down_color = data.getpixel((left,down))
                        right_color = data.getpixel((right,y))
                        right_up_color = data.getpixel((right,up))
                        right_down_color = data.getpixel((right,down))

                        # Remove the vertical line interference line
                        if down_color == 0:
                            if left_color == 255 and left_down_color == 255 and \
                                right_color == 255 and right_down_color == 255:
                                data.putpixel((x,y),255)

                        # Remove the horizontal line
                        elif right_color == 0:
                            if down_color == 255 and right_down_color == 255 and \
                                up_color == 255 and right_up_color == 255:
                                data.putpixel((x,y),255)



                    # Remove slash interference lines
                    if left_color == 255 and right_color == 255 \
                            and up_color == 255 and down_color == 255:
                        data.putpixel((x,y),255)
                else:
                    pass

                # Save the image after removing the interference line
                data.save("test.png","png")
    except:
        return False

def saveImage(filename,size):
    image = Image.new("1",size)
    draw = ImageDraw.Draw(image)

    for x in xrange(0,size[0]):
        for y in xrange(0,size[1]):
            draw.point((x,y),t2val[(x,y)])

    image.save(filename)

image = Image.open("./1.png").convert("L")
#pIx(image)
twoValue(image,130)
clearNoise(image,2,1)
saveImage("./5.png",image.size)
