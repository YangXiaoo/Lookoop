
clc;clear all;
pic = imread('00.jpg');
imshow(pic);
[x,y] = ginput(2);    %确定图像上的两点利用ginput函数，返回值是两点的坐标
pic_1 = imcrop(pic,[x(1),y(1),abs(x(1)-x(2)),abs(y(1)-y(2))]);

%利用imcrop函数对图像进行切割，输入参数是一个定点坐标，

%从该定点出发向右abs(x(1)-x(2))，向下abs(y(1)-y(2))的区域进行切割
subplot(1,2,1);
imshow(pic_1);
imwrite(pic_1,'1.jpg');                     
gausFilter = fspecial('gaussian',[1 1],1.5);  
new = imfilter(pic_1,gausFilter,'replicate');  
new = imadjust(new);
subplot(1,2,2);

imwrite(new,'pout.jpg');
imshow(new);