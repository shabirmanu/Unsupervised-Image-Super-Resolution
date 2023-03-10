from utilities.gaussian import *
from pretrained_model import *
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
from utilities.helpers import *
from metrics_calculator import *
from argparse import ArgumentParser
import tensorflow as tf


parser = ArgumentParser()
parser.add_argument('--config', type=str, default='../configs/config.yaml', help="testing configuration file")
args = parser.parse_args()
config = get_config(args.config)

project_root = os.getcwd()
dir_dataset = config['data_dir']
files_img = [os.path.join(dir_dataset, x) for x in os.listdir(dir_dataset)]
img= files_img[8]

# window_name = 'image sample'
# cv2.imshow(window_name,img)
# cv2.waitKey(0)

def sample_action1(in_img, config):
    print("here")
    return


def perform_action1(in_img, config):
    img,img_small=downsample(in_img, scale=0.4, plot=False)
    dir_pretrained_models = config['model_dir']
    os.listdir(dir_pretrained_models)
    img_upscaled=get_upscaled_images(img_small, filemodel_filepath, modelname, scale)
    out_imgs=design_upscale(img_small)
    save_img(out_imgs)
    #
    action_input_dataset = config['action1_input']
    out_file_img = [os.path.join(action_input_dataset, x) for x in os.listdir(dir_dataset)]
    input_img1 = cv2.imread(out_file_img[0], 1)
    input_img2 = cv2.imread(out_file_img[1], 1)
    #
    #
    comb = comb_img(input_img1,input_img2)
    psnr=psnr_calc(img,comb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return psnr
perform_action1(img,config)