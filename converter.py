import cv2
import numpy as np
from PIL import Image

img = cv2.imread("the-chameleon-po-5120x2880-15518.jpg") 

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
cv2.imshow("Gray Image", gray) 
cv2.waitKey(0) 

returnValue, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY) 
cv2.imshow("Thresh Image", thresh) 
cv2.waitKey(0) 

matrix_kernel = np.array([
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
], dtype=np.float32)

filtered = cv2.filter2D(thresh, -1, matrix_kernel) 
cv2.imshow("3x3 Average Filter", filtered)
cv2.waitKey(0)
cv2.destroyAllWindows() 

output = Image.fromarray(filtered) 
output.save("output.jpg")