%目标函数
function f = f_min(x);
B = 1520; 
T = 2.5;
f = 2*pi*x(1)*T*sqrt((B/2)^2+x(2)^2);
end

