import cv
from LSBSteg import LSBSteg

import sys
imagename=sys.argv[1]

im = cv.LoadImage(imagename)
steg = LSBSteg(im)
print steg.unhideText()
