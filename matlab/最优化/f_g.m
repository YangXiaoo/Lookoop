%约束函数
function [g,ceq] = f_g(x);
B = 1520; 
T = 2.5;
P = 294300;
E = 2.119e5;
sigma_y = 690;

Q = 0.5*P*sqrt((B/2)^2+x(2)^2)/x(2);
sigma = Q/(pi*T*x(1));
g(1) = sigma - sigma_y;
sigma_c = 0.125*pi^2*E*(x(1)^2+T^2)/((B/2)^2+x(2)^2);
g(2) = sigma - sigma_c;
g(3) = 200 -x(2);
g(4) = x(1) -140;
g(5) = 20 - x(1);
g(6) = x(2) - 1200;
ceq = [];
end