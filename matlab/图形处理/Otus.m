
%===================主函数==================
clc;
clear all;
img = imread('00.jpg'); 
[counts x] = imhist(img);  
[m n] = size(img);  
level = otsu(counts, m*n);  
 output = img;  
 output(output<level) = 0;  
output(output>=level) = 255;  
imshow(output)  
%=====================调用函数======================
function level = otsu(histogramCounts, total)  
sum0 = 0;  
w0 = 0;  
maximum = 0.0;  
total_value = sum((0:255).*histogramCounts');  
for ii=1:256
    w0 = w0 + histogramCounts(ii);  
    if (w0 == 0)  
        continue;  
    end  
    w1 = total - w0;  
    if (w1 == 0)  
        break;  
    end  
    sum0 = sum0 +  (ii-1) * histogramCounts(ii);  
    m0 = sum0 / w0;  
    m1 = (total_value - sum0) / w1;  
    icv = w0 * w1 * (m0 - m1) * (m0 - m1);  
    if ( icv >= maximum )  
        level = ii;  
        maximum = icv;  
    end  
end  
  
end