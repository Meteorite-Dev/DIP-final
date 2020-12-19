'''
Filter.py 
寫 filter 的地方，各式各樣的 filter
'''
from numpy import fft
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

    def Gaussian_filter(self , image ,intensity=10) :
        blur = cv2.GaussianBlur(image , (5,5) , intensity)
        return blur 

    def medianblur(self , image , size=5) :
        blur = cv2.medianBlur(image ,ksize=size)
        return blur

    def morphology(self ,image , filter, Opening=True) :
        if Opening :
            blur = cv2.morphologyEx(image , cv2.MORPH_OPEN , kernel=filter)
        else :
            blur = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel=filter)
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
        ret, Gimage = cv2.threshold(Gimage, 0, 255, cv2.THRESH_OTSU)
        return Gimage

    

    def blur(self , image , ins=5) :
        ins *=2
        image = cv2.blur(image , (ins,ins))
        
        return image
    
    # too bad
    def hist_equal(self , hsv_image) :
        # fftv = np.fft.fft(V)
        print(image.shape)
        image[:,:,2] = cv2.equalizeHist(image[:,:,2])
        return image

    # developing 
    def homomorphic(self ,hsv) :
        v = hsv[:,:,2]
        for i in range(v.shape[0]):
            for j in range(v.shape[1]):
                if v[i][j] ==0 :
                    v[i][j] +=1
        print(np.min(v) ,np.max(v))
        print(v.shape)
        log_v = np.log(np.float64(v), dtype=np.float64)
        dft = np.fft.fft2(log_v)
        dft_shift = np.fft.fftshift(dft)
        print(dft)

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
        image = super().Gaussian_filter(image, intensity=5)
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            pass
        can = cv2.Canny(image,100,200,apertureSize=3 , L2gradient=False)
        
        can  =cv2.convertScaleAbs(can)

        return can

if __name__ == "__main__" :
    fil = Filter()
    edg = EdgeDetector()
    im = Image_classical()
    image = im.OpenImage("source\\HDR.jpg" , methood="cv")
    
    hsv = im.RGB2HSV(image)
    v = fil.homomorphic(hsv)
    # image = im.HSV2RGB(hsv)
    # image = im.CV2PIL(v)
    # im.show(v , methood="cv")
