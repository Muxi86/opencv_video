import cv2
import numpy as np

print(cv2.__version__)

img = np.zeros((512,512,3), np.uint8)
cv2.circle(img,(256,256), 100, (0,0,255), 2)
cv2.imshow('Image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()