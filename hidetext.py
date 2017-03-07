import cv
from LSBSteg import LSBSteg
#Hide
str = "Hiding Text in an image"
import sys
imagename=sys.argv[1]
textstring=sys.argv[2]
carrier = cv.LoadImage(imagename)
steg = LSBSteg(carrier)
steg.hideText(textstring)
steg.saveImage(imagename + ".png") #Image that contain datas

