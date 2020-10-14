import cv2
import numpy as np
import matplotlib.pyplot as plt

def bai_1():
    I = cv2.imread("lion.jpg")
    J = cv2.imread("lionHSV.jpg")
    IJ = np.concatenate((I, J), axis = 1)
    plt.imshow(cv2.cvtColor(IJ, cv2.COLOR_BGR2RGB))
def bai_2():
    J = cv2.cvtColor(cv2.imread("lion.jpg"), cv2.COLOR_BGR2HSV).astype(np.double)
    h = J[:,:,0]/180
    for i in range(h.shape[0]):
        for j in range(h.shape[1]):
            if h[i][j] > 0.22 and h[i][j] < 0.45:
                h[i][j] = 1
            else:
                h[i][j] = 0
    cv2.imshow("h", h)
    cv2.waitKey(0)
def bai_3():
    R = cv2.cvtColor(cv2.imread("lion.jpg"), cv2.COLOR_BGR2RGB)
    data = np.loadtxt('data.txt').astype(np.uint8)
    B = np.ones((256,256,256), dtype=np.uint8)
    for d in data:
        B[d[0]][d[1]][d[2]] = d[3]
    for x in range(R.shape[0]):
        for y in range(R.shape[1]):
            if B[R[x][y][0]][R[x][y][1]][R[x][y][2]]:
                R[x][y] = np.zeros(3, dtype = np.uint8)
    plt.imshow(R)
if __name__ == "__main__":
    bai_1()
    bai_2()
    bai_3()