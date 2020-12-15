'''

這裡是寫基礎影像處理的部分，很難。
所以大家加油。

'''
from PIL import Image
import cv2
import numpy as np

from numpy.fft import fftn


class Image_classical():
    def __init__(self ) :
        self.image_file_name = ".\ImageProcess\okayu.png"

    def OpenImage(self, image_file_name =None , methood="cv"):
        methood = methood.lower()
        if methood =="cv" or methood =="cv2" :
            
            if image_file_name != None:
                print("open image with OpenCV : ", image_file_name)
                self.image = cv2.imread(image_file_name, cv2.IMREAD_COLOR)
                self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
                self.ImSize = self.image.shape[:2]
                return self.image
            else:
                print("open default image with OpenCV : ", image_file_name)
                self.image = cv2.imread(self.image_file_name, cv2.IMREAD_COLOR)
                self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
                self.ImSize = self.image.shape[:2]
                return self.image
        elif methood=="pil" :
            if image_file_name != None:
                print("open image :", image_file_name)
                self.image = Image.open(image_file_name)
                self.ImSize = self.image.size
                self.ImFormat = self.image.format
                self.ImMode = self.image.mode
                return self.image
            else:
                print("open image :", self.image_file_name)
                self.image = Image.open(self.image_file_name)
                self.ImSize = self.image.size
                self.ImFormat = self.image.format
                self.ImMode = self.image.mode
                return self.image


    def image_info_get(self  ,image , methood="pil"):
        methood = methood.lower()
        if methood == "pil":
            return image.size , image.mode
        elif methood =="cv2" or methood =="cv" :
            return image.shape[:2] , "RGB"
        elif methood =="hsi" :
            return image.shape[:2] , "HSI"
        elif methood =="np":
            return image.shape , "numpy_array"
        else :
            assert("Convert error : flag not found.")

    # 目前是有損轉換
    def show(self, image ,methood ="pil", rotate = 0 ,trans=False):
        methood = methood.lower()
        if methood =="pil" :
            if trans :
                image = image.transpose(Image.FLIP_LEFT_RIGHT)
            if rotate !=0 :
                image = image.rotate(rotate)
            image.show()
        elif methood =="cv" or methood =="cv2":
            if trans :
                image = cv2.flip(image, 1)
            if rotate != 0 :
                center = (image.shape[0]/2 , image.shape[1]/2)
                rot = cv2.getRotationMatrix2D(center, rotate, 1)
                image = cv2.warpAffine(image, rot, image.shape[:2])
            cv2.imshow("image", image)
            cv2.waitKey()
            cv2.destroyAllWindows()


    def SaveImage(self, image , name, path=None):
        if path == None:
            path = ""
        else:
           path = str(path)+"\\"
        all_path = path+str(name)+"."+str.lower(str(self.ImFormat))
        print("save image : " ,all_path )
        image.save(all_path)
        
    def ResizeImage(self ,image , devide , methood="cv"):
        methood = methood.lower()
        if methood =="cv" or methood =="cv2" :
            H,W = image.shape[:2]
            size = (int(W/devide) , int(H/devide)  )
            print(size)
            Rimage = cv2.resize(image , size )
            return Rimage
        elif methood =="pil":
            W,H = image.size
            size = (int(W/devide) , int(H/devide)  )
            Rimage = image.resize(size,Image.ANTIALIAS)
            return Rimage
    
    def PIL2CV(self ,image ):
        CVimage = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
        CVimage =  cv2.cvtColor(CVimage, cv2.COLOR_BGR2RGB)
        return CVimage

    def CV2PIL(self , image) :
        self.image = Image.fromarray(image)
        return self.image

    def img2np(self ,image, methood="cv") : 
        methood = methood.lower()
        if methood == "cv" or methood == "cv2" :
            # cv to numpy
            image_arr  = np.array(image)
            return image_arr
        elif methood == "pil" :
            # PIL to numpy
            image = self.PIL2CV(image = image)
            image_arr =np.array(image)
            return image_arr
        else :
            assert("Convert error : flag not found.")

    def np2PIL(self , np_array ):
        image = Image.fromarray(np.uint8(np_array)).convert('RGB')
        # image = self.CV2PIL(image=np_array)
        return image

    def fft(self ,image_arr):
        fft_array = fftn(image_arr)
        fft_array = np.abs(fft_array)
        return fft_array

    #　速度很慢的　　RGB to HSI
    # 抄起來
    def RGB2HSI(self ,rgb_img):
        with np.errstate(divide='ignore', invalid='ignore'):
        
            row = np.shape(rgb_img)[0]
            col = np.shape(rgb_img)[1]
            
            hsi_img = rgb_img.copy()
            
            B, G, R = cv2.split(rgb_img)
            
            [B, G, R] = [i / 255.0 for i in ([B, G, R])]
            H = np.zeros((row, col))  
            I = (R + G + B) / 3.0  
            S = np.zeros((row, col))  
            for i in range(row):
                den = np.sqrt((R[i]-G[i])**2+(R[i]-B[i])*(G[i]-B[i]))
                thetha = np.arccos(0.5*(R[i]-B[i]+R[i]-G[i])/den)  
                h = np.zeros(col)  
                
                h[B[i] <= G[i]] = thetha[B[i] <= G[i]]
                
                h[G[i] < B[i]] = 2*np.pi-thetha[G[i] < B[i]]
                
                h[den == 0] = 0
                H[i] = h/(2*np.pi) 
            
            for i in range(row):
                min = []
                
                for j in range(col):
                    arr = [B[i][j], G[i][j], R[i][j]]
                    min.append(np.min(arr))
                min = np.array(min)
                
                S[i] = 1 - min*3/(R[i]+B[i]+G[i])
                
                S[i][R[i]+B[i]+G[i] == 0] = 0
            
            hsi_img[:, :, 0] = H*255
            hsi_img[:, :, 1] = S*255
            hsi_img[:, :, 2] = I*255
            return hsi_img

    # 抄起來
    def HSI2RGB(self, hsi_img):
        with np.errstate(divide='ignore', invalid='ignore'):    
            row = np.shape(hsi_img)[0]
            
            rgb_img = hsi_img.copy()
            
            H, S, I = cv2.split(hsi_img)
            
            [H, S, I] = [i / 255.0 for i in ([H, S, I])]
            R, G, B = H, S, I
            for i in range(row):
                h = H[i]*2*np.pi
                
                a1 = h >= 0
                a2 = h < 2*np.pi/3
                a = a1 & a2
                tmp = np.cos(np.pi / 3 - h)
                b = I[i] * (1 - S[i])
                r = I[i]*(1+S[i]*np.cos(h)/tmp)
                g = 3*I[i]-r-b
                B[i][a] = b[a]
                R[i][a] = r[a]
                G[i][a] = g[a]
                
                a1 = h >= 2*np.pi/3
                a2 = h < 4*np.pi/3
                a = a1 & a2 
                tmp = np.cos(np.pi - h)
                r = I[i] * (1 - S[i])
                g = I[i]*(1+S[i]*np.cos(h-2*np.pi/3)/tmp)
                b = 3 * I[i] - r - g
                R[i][a] = r[a]
                G[i][a] = g[a]
                B[i][a] = b[a]
                
                a1 = h >= 4 * np.pi / 3
                a2 = h < 2 * np.pi
                a = a1 & a2 
                tmp = np.cos(5 * np.pi / 3 - h)
                g = I[i] * (1-S[i])
                b = I[i]*(1+S[i]*np.cos(h-4*np.pi/3)/tmp)
                r = 3 * I[i] - g - b
                B[i][a] = b[a]
                G[i][a] = g[a]
                R[i][a] = r[a]
            rgb_img[:, :, 0] = B*255
            rgb_img[:, :, 1] = G*255
            rgb_img[:, :, 2] = R*255
            return rgb_img
    
    def RGB2YCrCb(self ,rgb_image) :
        CrCb = cv2.cvtColor(rgb_image , cv2.COLOR_RGB2YCrCb)
        return CrCb
    
    def YCrCb2RGB(self , crcb_image):
        RGB = cv2.cvtColor(crcb_image , cv2.COLOR_YCrCb2RGB)
        return RGB
    
    def RGB2HSV(self , image):
        HSV = cv2.cvtColor(image , cv2.COLOR_RGB2HSV)
        return HSV

    def HSV2RGB(self , HSV) :
        RGB = cv2.cvtColor(HSV , cv2.COLOR_HSV2RGB) 
        return RGB   


if __name__ =='__main__' :
    im = Image_classical()
    image = im.OpenImage(image_file_name="okayu.png" , methood="pil")
    image = im.ResizeImage(image, 3 , methood="pil")
    im.show(image, methood="pil")

