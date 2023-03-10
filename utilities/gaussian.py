#first we will design gaussian pyramid
import cv2
import numpy as np
import os
from utilities.manage_config import get_config

# config = get_config("/configs/config.yaml")
# project_root = os.getcwd()
# dir_dataset = config['action1_input']
#
# file_img = [os.path.join(dir_dataset, x) for x in os.listdir(dir_dataset)]
# input_img1 = cv2.imread(file_img[0], 1)
# input_img2 = cv2.imread(file_img[1], 1)
# #input_img3= cv2.imread(file_img[2],1)

def comb_img(img1,img2):
    comb = cv2.addWeighted(img1, 0.6,img2, 0.4, 0.0)
    cv2.imwrite('action_1_output/weighted32.png', comb)
    print(cv2.imshow("comb",comb))
    return comb








#
#
#
# #downsampled  output1
# first_layer= cv2.pyrDown(input_img1)
# second_layer= cv2.pyrDown(first_layer)
#
# #for 2 image
# first_layer2 = cv2.pyrDown(input_img2)
# second_layer2= cv2.pyrDown(first_layer2)
#
# #combination
# comb= cv2.addWeighted(input_img1,0.3, input_img2,0.7, 0.0)
#
# #laplacian pyramid
# #expanding image
# expand_image_first_l=  cv2.pyrUp(first_layer)
# expand_image_second_l=  cv2.pyrUp(second_layer)
#
# #expanding image2
# expand_image_first_l2=  cv2.pyrUp(first_layer2)
# expand_image_second_l2=  cv2.pyrUp(second_layer2)
#
# #laplacian
# laplacian11 = cv2.subtract(input_img1, expand_image_first_l)
# laplacian12 = cv2.subtract(first_layer, expand_image_second_l)
#
# #laplacian 2
# laplacian21 = cv2.subtract(input_img2, expand_image_first_l2)
# laplacian22 = cv2.subtract(first_layer2, expand_image_second_l2)
# #if in case to ccheck the size of images
# #but this dataset has same size images(384,384)
# #print(laplacian22.shape)
#
# final_lap1= cv2.add(laplacian11,laplacian21)
# final_lap2 =cv2.add(laplacian12,laplacian22)
# #we need this image to reconstruct  the image
# final_gauss=  cv2.add(second_layer,second_layer2)
#
# # #to reconstruct image
# reconstruct1=cv2.pyrUp(final_lap1)
# reconstruct2=cv2.pyrUp(final_lap2)
#
# reconstruct = [reconstruct1, reconstruct2]
#
# laplacian = [final_lap1,final_lap2]
#
# reconstruct_image1 = cv2.add(reconstruct2, final_lap1)
# print(input_img2.shape)
# #final_comb=cv2.add( comb,reconstruct2)
# cv2.imwrite('action_1_output/weighted3.png',comb)
# #cv2.imshow("action1 final img",final_comb)
# cv2.imshow("comb",comb)
#
#
# #display expanded img
# # cv2.imshow("exp1",expand_image_first_l)
#
# #
#
# #to display  images
# #cv2.imshow("first downsampled",first_layer)
# #cv2.imshow("second downsampled",second_layer)
# # cv2.imshow("Ground Truth",input_img1)
#
# comb_img(input_img1,input_img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()