#first we will design gaussian pyramid
import cv2
import numpy as np
import os

project_root = os.getcwd()
dir_dataset = os.path.join(project_root, "HR")

input_img1 = cv2.imread("C:\\Users\\aashi\\Unsupervised-Image-Super-Resolution\\HR\\0.png")
input_img2 = cv2.imread("C:\\Users\\aashi\\Unsupervised-Image-Super-Resolution\\HR\\17.png")

#downsampled  output1
first_layer= cv2.pyrDown(input_img1)
second_layer= cv2.pyrDown(first_layer)

#for 2 image
first_layer2 = cv2.pyrDown(input_img2)
second_layer2= cv2.pyrDown(first_layer2)

#laplacian pyramid
#expanding image
expand_image_first_l=  cv2.pyrUp(first_layer)
expand_image_second_l=  cv2.pyrUp(second_layer)

#expanding image2
expand_image_first_l2=  cv2.pyrUp(first_layer2)
expand_image_second_l2=  cv2.pyrUp(second_layer2)

#laplacian
laplacian11 = cv2.subtract(input_img1, expand_image_first_l)
laplacian12 = cv2.subtract(first_layer, expand_image_second_l)

#laplacian 2
laplacian21 = cv2.subtract(input_img2, expand_image_first_l2)
laplacian22 = cv2.subtract(first_layer2, expand_image_second_l2)

cv2.imshow("lap2",laplacian21)

#display expanded img
# cv2.imshow("exp1",expand_image_first_l)



#to display  images
#cv2.imshow("first downsampled",first_layer)
#cv2.imshow("second downsampled",second_layer)
# cv2.imshow("Ground Truth",input_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()