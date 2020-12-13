'''
Filter.py 
寫 filter 的地方，各式各樣的 filter
'''
from IM_classical import Image_classical
import numpy as np 
import cv2

class Filter():
    def __init__ (self):
        pass
    
    def gaussian_kernal(self, size, intensity = 0.5):
        gs_ker = cv2.getGaussianKernel(ksize=size , sigma=intensity)
        gs = gs_ker * gs_ker.T

        return gs
    
    def Gaussian_filter(self , image ,intensity=2) :
        blur = cv2.GaussianBlur(image , (5,5) , intensity)
        return blur 

    def filter2d(self , image , filter ):
        for i in range(3):
            image[i] = cv2.filter2D(image[i] , -1 , filter)
        return image
    
    def otsu_threshold(self , image ) :
        image = self.Gaussian_filter(image, intensity=0.5)
        if len(image.shape) ==3 :
            Gimage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else :
            Gimage = image
        ret, Gimage = cv2.threshold(Gimage, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        return Gimage

class EdgeDetector(Filter):
    def __init__(self) :
        Filter.__init__(self)
        self.ddepth = cv2.CV_16S
    
    def LoG(self , image ):
        image = super().Gaussian_filter(image , intensity=0.5)
        if len(image.shape) == 3:
            Gimage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            Gimage = image
        LOG = cv2.Laplacian(Gimage , ddepth=self.ddepth , ksize=3)
        LOG = cv2.convertScaleAbs(LOG)
        return LOG

    def Sobel(self, image) :
        image = super().Gaussian_filter(image, intensity=0.5)
        if len(image.shape) == 3:
            Gimage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            Gimage = image
        
        grad_x = cv2.Sobel(Gimage, self.ddepth ,1 ,0 , ksize=3 , scale=1 , delta=0 , borderType=cv2.BORDER_DEFAULT)
        grad_y = cv2.Sobel(Gimage, self.ddepth, 0, 1, ksize=3 ,scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)

        grad_x = cv2.convertScaleAbs(grad_x)
        grad_y = cv2.convertScaleAbs(grad_y)

        grad = cv2.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)

        return grad

    def Canny(self, image) :
        image = super().Gaussian_filter(image, intensity=0.5)
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            pass
        can = cv2.Canny(image, apertureSize=3 , L2gradient=False)
        
        can  =cv2.convertScaleAbs(can)

        return can

if __name__ == "__main__" :
    fil = Filter()
    im = Image_classical()
    image = im.OpenImage("okayu.png" , methood="cv")
    image = fil.otsu_threshold(image)
    image = im.CV2PIL(image)
    im.show(image)
