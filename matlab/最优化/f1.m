%目标函数
%f1.m
function f=f1(x)
B = 1520; %人字架跨距
T = 2.5; %钢管厚度
f = 2*pi*x(1)*T*sqrt((B/2)^2+x(2)^2);