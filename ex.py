import numpy as np
import cv2
#import convolute_lib as cnn
def cal_hist(image):
    for p in range(0, 256):
        for i in range(rows):
            for j in range(cols):
                if(G[i][j] == p):
                    count = count + 1
        histogram[p] = count
        count = 0
    hgr = np.zeros(256)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            hgr[image[x][y]] += 1
    return hgr
print(np.zeros(256).shape)