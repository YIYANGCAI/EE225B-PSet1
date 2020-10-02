import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

class histogramAnalysis():
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
        #self.ax.hist(data,bins=256,histtype="stepfilled",density=flag,alpha=0.6)
        #self.fig.savefig(figure_path, dpi=200)

if __name__ == "__main__":
    s = histogramAnalysis('./rose1024.tif')
    print("drawing the histogram, the diagram is saved in the same direction of program")
    s.imageHist4e(s.img_gray, mode='n')