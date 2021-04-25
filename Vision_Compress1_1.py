#!/usr/bin/env python
# coding: utf-8

import numpy as np
import cv2
import os 

image = cv2.imread('foreman_qcif_0_rgb.bmp')
matrix = np.array(
        [[.299, .587, .114], [-.168736, -.331264, .5], [.5, -.418688, -.081312]])


def rgb2ycbcr(img):
    mat  = matrix
    ycbcr = img.dot(mat.T)
    ycbcr[:, :, [1]] += 128
    ycbcr[:, :, [2]] += 128
    return np.uint8(ycbcr)




def ycbcr2rgb(img):
    mat  = np.linalg.inv(matrix)
    img = img.astype(np.float64)
#     mat = np.array([[1, 0, 1.402], [1, -0.34414, -.71414], [1, 1.772, 0]])
    img[:,:,[1]] -= 128
    img[:,:,[2]] -= 128
    ret = img.dot(mat.T)
    np.putmask(ret, ret > 255, 255)
    np.putmask(ret, ret < 0, 0)
    return np.uint8(ret)


def subsampling(img):
    img[1::2, :] = img[::2, :] 
    img[:, 1::2] = img[:, ::2]
    return img 




ycbcr = rgb2ycbcr(image) #change mode





y = ycbcr[:, :, 0] 
cb = ycbcr[:, :, 1] 
cr = ycbcr[:, :, 2] 



os.mkdir('./1')
cv2.imwrite("1/hw1_ycbcr.bmp", ycbcr) 
cv2.imwrite("1/hw1_y.bmp", y) 
cv2.imwrite("1/hw1_cb.bmp", cb) 
cv2.imwrite("1/hw1_cr.bmp", cr) 





cb_subsample = subsampling(cb) 
cr_subsample = subsampling(cr) 


cv2.imwrite("1/hw1_cb_subsampe.bmp", cb_subsample) 
cv2.imwrite("1/hw1_cr_subsampe.bmp", cr_subsample) 

#merge 三維資料
ycbcr_subsample = cv2.merge((y, cb_subsample, cr_subsample)) 
rgb_subsample = ycbcr2rgb(ycbcr_subsample) 
cv2.imwrite("1/hw1_rgb_subsample.bmp", rgb_subsample)

