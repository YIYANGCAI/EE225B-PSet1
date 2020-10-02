from scipy.stats import moment
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

class centralMoments():
    def __init__(self, img_path):
        self.img = cv.imread(img_path)
        self.w, self.h = self.img.shape[0:2]
        self.img_gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        self.fig, self.ax=plt.subplots()
        self.init_hist = np.zeros(256)
        self.norm_hist = np.zeros(256)
    
    def imageHist4e(self, img, mode = 'n'):
        flag = True
        figure_path = './hist_norm.tif'
        if mode == 'u': 
            flag = False
            figure_path = './hist_ori.tif'

        data = img.flatten()
        for pixel in list(data):
            self.init_hist[pixel] = self.init_hist[pixel] + 1
        
        if flag:
            bar_data = list(self.init_hist/(self.h * self.w))
            plt.bar(range(0, 256), bar_data)
            plt.savefig(figure_path)
        else:
            bar_data = list(self.init_hist)
            plt.bar(range(0, 256), bar_data)
            plt.savefig(figure_path)
        
    def display(self, img, name):
        cv.namedWindow(name, cv.WINDOW_AUTOSIZE)
        cv.imshow(name, img)
        cv.waitKey(0)
        cv.destroyAllWindows()
    
    def centralMoments4e(self, img, n):
        moments = []
        data = img.flatten()
        for i in range(n):
            moments.append(moment(data, moment=(i+1)))
        return moments

if __name__ == "__main__":
    s1 = centralMoments('./rose1024.tif')
    s2 = centralMoments('./angiography_live_image.tif')

    # calculate the moment and dispay the image
    print("The 4 moments of image rose\n{}".format(s1.centralMoments4e(s1.img_gray, 4)))
    s1.display(s1.img_gray, 'rose')
    print("The 4 moments of image angiography_live_ image\n{}".format(s2.centralMoments4e(s2.img_gray, 4)))
    s2.display(s2.img_gray, 'angiography_live')

    # histogram, default to be normalized
    print("drawing the histogram, the diagram is saved in the same direction of program")
    print('yellow is rose, blue is angiography_live_ image')
    s2.imageHist4e(s2.img_gray, mode='n')
    s1.imageHist4e(s1.img_gray, mode='n')
    
