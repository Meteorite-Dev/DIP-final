'''
寫圖表產生的地方，包含3d 和 2d 圖表


'''
from matplotlib import pyplot as plt
from mayavi import mlab
from scipy import stats as stats

from imError import ChannelError
import numpy as np

# test 用的
from IM_classical import Image_classical


class plot2D() :
    def __init__(self) :
        pass

    def third_channel_his(self, np_array, title="historgram", legend="RGB"):
        sh = len(np_array.shape)
        fig = plt.figure()
        try :
            if sh!=3 :
                raise ChannelError
        except ChannelError :
            raise RuntimeError("ChannelError : dimension not 3.")

        arlist = np.dsplit(np_array ,3)
        for i in range(3):
            arlist[i] = arlist[i].flatten()
        
        kwargs = dict(histtype='stepfilled', alpha=0.3, density=True, bins=40) 
        
        plt.title(title)
        
        plt.hist(arlist[0], **kwargs) 
        plt.hist(arlist[1], **kwargs) 
        plt.hist(arlist[2], **kwargs)
        legend = list(legend)
        plt.legend(legend , loc='best')
        # plt.show()
        fig.canvas.draw()
        
        img = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        return img

    def RGB_plot(self , image) :
        image  = self.third_channel_his(np_array=image , title="Historgram of RGB " , legend="RGB")
        return image
    
    def HSI_plot(self , image) :
        image = self.third_channel_his(np_array=image , title="Historgram of HSI " , legend="HSI")
        return image
    
    def HSV_plot(self, image):
        image = self.third_channel_his(np_array=image, title="Historgram of HSV ", legend="HSV")
        return image

    def YCrCb_plot(self, image):
        image = self.third_channel_his(np_array=image, title="Historgram of YCrCb ", legend=("Y","Cr","Cb"))
        return image

class plot3D():
    def __init__(self) :
        pass
    
    # 照片小於 256*256 不然會算很久
    def three_channel_his_3D(self ,np_array):
        sh = len(np_array.shape)
        try :
            if sh!=3 :
                raise ChannelError
        except ChannelError :
            raise RuntimeError("ChannelError : dimension not 3.")
        
        arlist = np.dsplit(np_array, 3)
        for i in range(3):
            arlist[i] = arlist[i].flatten()
            print(arlist[i].shape)
        
        stack_array = np.vstack([arlist[0] ,arlist[1] , arlist[2]])
        density = stats.gaussian_kde(stack_array)(stack_array)
        figure = mlab.figure('DensityPlot')
        pts = mlab.points3d(
            arlist[0], arlist[1], arlist[2], density, scale_mode='none', scale_factor=0.5)

        mlab.axes()
        mlab.show()

if __name__ =="__main__" :
    im = Image_classical()
    image = im.OpenImage("source\\okayu.png" ,methood="cv")
    image = im.ResizeImage(image,devide=10 , methood="cv")
    np_array = im.img2np(image,methood="cv")

    plot= plot2D()
    image = plot.RGB_plot(np_array)
    im.show(image , methood="cv")
