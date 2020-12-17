# Final Project 
> author : Ming

## 最終呈現
有一個 GUI 然後可以對輸入的影像作出增強，去模糊，然後去提取它的特徵，把一部分的 convolution 影像化。

### 目前進行的工作

明哲 : 正在寫程式(影像處理部分)\
Boboxin：加入寫程式行列(前端GUI介面)

缺少 : GUI 介面的設計工程師、影像處理工程師

廣徵人才中!!!!


## 注意
在寫程式之前，請先了解其他程式碼，大致上知道他在幹嘛就好了。

程式部分包含三個部分 : 
1. GUI 介面 : 用的是 tkinter
2. 中介層，也就是 GUI 各元件背後的 function
3. 影像處理層 : 雖然現在只有一個，但是會把它分成基礎的處理跟複雜的處理，可能會有好幾個檔案。使用的是 pillow 和 opencv-python==4.2.0.32
4. 如果可以，要寫註解
5. 影像處理相關的 已經移到 ImageProcess 底下，預測大概會有很多。

希望大家都能加油。

## 更新紀錄
> 在有更新的時候，請記得打一下這個。
> 務必要告訴其他人新增的地方。
> 重大進展：放上背景，可以把案件放在背景圖片上面，缺少1024*720的GIF圖


12/16

重要背景已加入，按鈕皆已放置到定位，甚至button也設置了造型，圖片也可以直接顯示在畫面上，目前規劃checksum讓button可以多功能傑在圖片上面。

12/13

完成背景放置，等到1024*720gif圖進來後可以將按鈕擺放到定位


12/9 

寫完 sobel canny otsu 都是 call function 還蠻簡單的。\
也搞定 plot 3D 不過那個要圖片好小不然就是你的電腦夠強

12/8

寫完 histogram 然後增加可以使用的錯誤的資訊 \
寫了一個 API.md 可以給需要的人看有甚麼可以用

然後，急需 **碼農** 我快死掉了 by Ming

12/5 

搞定 HSI 了 順便把 YCrCb 搞定，然後把影像處理的 module 化 \
開始 HDR 跟 filter ，可能需要先來個 高斯函樹或是三小的 by Ming\
開始寫 filter 類型的東西 高斯已經初步完成(反正都是 call function)
 
12/1 嘗試 fft 但確定需要轉換，需要考慮轉換成什麼? ( YCrCb , HIS , YIQ ) 
     需要 HDR 濾波增強，模糊處理，historgram，convolution(特徵提取) by Ming

11/24 新增 README.md 對所有資料做出說明 by Ming 



## 待完成


**Edge detector**
LOG (Laplacian of gaussian)
canny 
sobel (一階) 

**plot and statistics**
3D plot 

**convolution**
conv2D
padding

**other**
HDR
otsu's -> 取閥值 
**GUI**
非常多的東西
