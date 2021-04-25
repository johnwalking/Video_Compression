import numpy as np
import cv2
import os 
import io



matrix = np.array(
        [[.299, .587, .114], [-.168736, -.331264, .5], [.5, -.418688, -.081312]])




def ycbcr2yuv(y, cb, cr):
    y_byte = bytearray(y)
    cb_byte = bytearray(cb)
    cr_byte = bytearray(cr)
    yuv_byte = bytearray()
    #yuv_byte = y_byte + cb_byte + cr_byte
    yuv_byte = y_byte + cr_byte + cb_byte
    return yuv_byte




def rgb2ycbcr(img):
    mat  = matrix
    ycbcr = img.dot(mat.T)
    ycbcr[:, :, [1]] += 128
    ycbcr[:, :, [2]] += 128
    return np.uint8(ycbcr)



def ycbcr2rgb(img):
    mat  = np.linalg.inv(matrix)
    img = img.astype(np.float64)
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

def process(imgPath):
    img = cv2.imread(imgPath)
    ycbcr = rgb2ycbcr(img)
    y = ycbcr[:, :, 0]
    cb = ycbcr[:, :, 1]
    cr = ycbcr[:, :, 2]
    cb_subsample = subsampling(cb)
    cr_subsample = subsampling(cr)
    num = imgPath.split("_")[2]
    cv2.imwrite('2/'+ 'hw1_' + str(num) + '_y.bmp', y)
    cv2.imwrite('2/'+ 'hw1_' + str(num) + '_u.bmp', cb_subsample)
    cv2.imwrite('2/'+ 'hw1_' + str(num) + '_v.bmp', cr_subsample)
    return ycbcr2yuv(y, cb_subsample, cr_subsample)




os.mkdir('./2')
img0 = process("foreman_qcif_0_rgb.bmp")
img1 = process("foreman_qcif_1_rgb.bmp")
img2 = process("foreman_qcif_2_rgb.bmp")

with io.open("2/output.yuv","wb") as fp:
    output = img0 + img1 + img2
    fp.write(output)
