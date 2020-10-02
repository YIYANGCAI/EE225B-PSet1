import numpy as np
import cv2 as cv

class DenoiseSolution():
    def imread(self, path):
        img = cv.imread(path)
        return img
    
    def imsave(self, path, img):
        cv.imwrite(path, img)

    def rgb2gray(self, img):
        return cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    
    def gaussian_filter(self, img, k_size):
        return cv.GaussianBlur(img, (k_size,k_size), 0) 
    
    def median_filter(self, img, k_size):
        return cv.medianBlur(img, k_size)

    def fft_filter(self, img, lfp_ratio):
        if len(img.shape) > 2: img = self.rgb2gray(img)
        rows, cols = img.shape
        f = np.fft.fft2(img)
        fshift = np.fft.fftshift(f)

        mask = np.zeros((rows, cols))
        crow = int(rows/2)
        ccol = int(cols/2)
        # rectangle mask
        #mask[crow-int(crow*lfp_ratio):crow+int(crow*lfp_ratio), ccol-int(ccol*lfp_ratio):ccol+int(ccol*lfp_ratio)] = 1
        mask[:, ccol-int(ccol*lfp_ratio):ccol+int(ccol*lfp_ratio)] = 1

        fshift = fshift * mask

        f_ishift = np.fft.ifftshift(fshift)
        img_back = np.fft.ifft2(f_ishift)
        img_back = np.abs(img_back)
        return img_back
    
    def visualize_f(self, img):
        if len(img.shape) > 2: img = self.rgb2gray(img)
        f = np.fft.fft2(img)
        fshift = np.fft.fftshift(f)
        mag = 20*np.log(np.abs(fshift))
        self.imsave('./mag.tif', mag)

def main():
    solution = DenoiseSolution()
    img = solution.imread('./apollo 17_boulder_noisy.tif')
    img_processed = solution.median_filter(img, 7)
    img_processed = solution.gaussian_filter(img, 7)
    img_processed = solution.fft_filter(img_processed, 0.2)
    print("the result are saved in the same direction of program")
    solution.imsave('./result.tif', img_processed)

if __name__ == "__main__":
    main()