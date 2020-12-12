## APIs

## IM_classical

```python 
#define
from ImageProgress.IM_classical import . 
Image_classical = IM_classical.Image_classical()
```

**開啟圖片**
```python
image = Image_classical.OpenImage(image_file_name =None , methood="cv")
```
image_file_name : image_path 

methood         : cv or pil

**圖片資訊**
```python 
(image_size , mode) = Image_classical.image_info_get(image , methood="pil")
```
image : 輸入 圖片

methood : CV (RGB) , pil , np , hsi

**顯示圖片**
```python
Image_classical.show(image ,methood ="pil", rotate = 0 ,trans=False)
```
image : image 

methood : cv or pil 

rotate : 旋轉 [-360 , 360]

trans : 水平翻轉 False or True


**圖片儲存**
```python
Image_classical.SaveImage(image , name, path=None)
```
待修正

**圖片大小調整**
```python
Image_classical.ResizeImage(image , devide , methood="cv")
```
devide : 減少的倍率

methood : cv or pil 

*有損，可能顏色會不對

**圖片轉換型態轉換**

> pil to cv
```python
# rgb transfer
pillow_image  = Image_classical.PIL2CV(image)
```

> cv to pil
```python
#rgb transfer
CV_image = Image_classical.CV2PIL(image)
```

> img to np 
```python
#transfer to np array (3 channel)
np_array = Image_classical.img2np(image, methood="cv")
```
methood : cv or pil


> np to pil 
```python
#np to pil 
pil_image = Image_classical.np2PIL(np_array)
```
* cv 可以直接顯示 np 的 但是 pil 不行

> 傅立葉變換
```python
#fft transfer  
fft_array = Image_classical.fft(np_array)
```
* 只接受 np_array

> RGB 2 HSI
```python
# HSI transfer  
# 速度慢，請盡量不要用
HSI = Image_classical.RGB2HSI(rgb_img)

RGB  = Image_classical.HSI2RGB(hsi_img)
```

> RGB to YCrCb
```python
#YCrCb transfer 
ycrcb = Image_classical.RGB2YCrCb(RGB_image)

RGB = Image_classical.YCrCb2RGB(crcb_image)
```

> RGB to HSV
```python
#HSV transfer 
HSV = Image_classical.RRGB2HSV(RGB_image)

RGB = Image_classical.HSV2RGB(HSV_image)
```
* 請盡量使用 HSV 的轉換，除非一定需要，不然不要用 HSI

## Filter

```python
#define
from ImageProgress.Filter import . 
filter =Filter.Filter()
EdgeDetector = Filter.EdgeDetector()
```

**產生高斯矩陣**
```python
高斯 矩陣
gs = Filter.gaussian_kernal(size ,intensity = 0)
```
size : 矩陣大小 col or row 的數值即可
* 此矩陣是正方形的
  
intensity : 矩陣數值 (正中間) ， 會自動產生周圍的

**高斯 filter**
```python
高斯模糊
blur_image = Filter.Gaussian_filter(image , intensity=0.5)
```
intensity : 模糊強度


**Filter 自訂義**
```python
image = Filter.filter2d(image , filter )
```
filter : 正方形矩陣， np 格式
* for 3 Channel image
  
**otsu_threshold**
```python
CV_image =  Filter.otsu_threshold(image)
```
* 圖片黑白分割(只有黑跟白)

**LoG**
```python
CV_image = EdgeDetector.LoG(image)
```
**Sobel**
```python
CV_image = EdgeDetector.Sobel(image)
```
**Canny**
```python
CV_image = EdgeDetector.Canny(image)
```
* 圖片會變成黑白的有線條的，就是畫線 
* 方式不一樣，參數的部分要到程式碼內部調整
* 基本上就是 call function 並不難



## plot 

```python
#define
from ImageProgress.plot import . 
# for x-y 
plot = plot.plot2D()
# for x-y-z
plot = plot.plot3D()
```
* 分為 3d 圖像及 2d 圖像
  
**3維 Historgram 產生**
```python
plot_cv_image = plot2D.third_channel_his(np_array , title , legend )
```
title : 圖表的開頭(圖名) default -> "historgram"  
legend : 圖表的圖例名稱 default -> "RGB"

return 是一個 cv image 

* 這是可以給你客製化需求。

**RGB plot**
```python  
RGG_plot_cv_image = plot2D.RGB_plot(image)
```
* 就是 RGB 的 historgram 

**HSI plot**
```python  
HSI_plot_cv_image = plot2D.HSI_plot(image)
```
* 就是 HSI 的 historgram 

**HSV plot**
```python  
HSV_plot_cv_image = plot2D.HSI_plot(image)
```
* 就是 HSV 的 historgram 

**YCrCb plot**
```python
YCrCb_plot_cv_image = plot2D.YCrCb_plot(image)
```
* 就是 YCrCb 的 historgram 


**3D plot**
```python
import mayavi
YCrCb_plot_cv_image = plot.three_channel_his_3D(np_array)
```
* 這個是三維的 ，需要新的套件，跟圖片資訊要小