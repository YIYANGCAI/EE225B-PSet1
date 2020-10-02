import cv2 as cv
import numpy as np

class Solution():
    def imread(self, path):
        return cv.imread(path)
    
    def gray(self, img):
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    def find_range(self, img):
        return img.min(), img.max()

    def imsave(self, path, img):
        cv.imwrite(path, img)

    def subtract(self, img1, img2):
        min_1, max_1 = self.find_range(img1)
        min_2, max_2 = self.find_range(img2)
        img1_scaled = (img1-min_1) / (max_1-min_1) * 256
        img2_scaled = (img2-min_2) / (max_2-min_2) * 256
        img_residual = (img1_scaled - img2_scaled) + 1
        _min, _max = self.find_range(img_residual)
        img_residual_scaled = (img_residual - _min) / (_max - _min) * 256
        return img_residual_scaled

if __name__ == "__main__":
    s = Solution()
    img_1 = s.imread('./angiography_live_image.tif')
    img_2 = s.imread('./angiography_mask_image.tif')
    
    img_3 = s.subtract(img_1, img_2)
    img_4 = s.subtract(img_2, img_1)

    print("the results are saved in the same direction of program")
    s.imsave('./result.tif', img_3)
    s.imsave('./result_reverse.tif', img_4)