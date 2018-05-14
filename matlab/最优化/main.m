%主程序
%设计变量(钢管平均直径D和人字架高度H)的初始值
x0 = [100;800];
%设计变量(钢管平均直径D和人字架高度H)的下界与上界
Lb = [20;200];
Ub = [140;1200];

%调用优化函数
%关闭大规模方式，显示优化过程的每次计算结果
options = optimset('largescale','off','display','iter');
%exitflag返回算法的终止标志
[x,fn,exitflag,output] = fmincon(@f_min,x0,[],[],[],[],Lb,Ub,@f_g,options);
disp('	********** 人字架尺寸优化设计最优解 ********** 	');
fprintf('	钢管平均直径 	D = %3.4f mm\n',x(1))
fprintf('	  人字架高度	H = %3.4f mm\n',x(2))
fprintf('	  人字架体积	V = %3.4f mm^3\n',fn)

%调用约束函数计算最优点x*的性能约束函数值
g = f_g(x);
disp(' 	********** 最优结果 **********	');
fprintf('人字架钢管压缩强度	 g1 = %3.4f MPa\n',g(1))
fprintf('  人字架钢管稳定性  g2 = %3.4f MPa\n',g(2))


%目标函数
function f = f_min(x);
B = 1520; T = 2.5;
f = 2*pi*x(1)*T*sqrt((B/2)^2+x(2)^2);

%约束函数
function [g,ceq] = f_g(x);
B = 1520; 
T = 2.5;
P = 294300;
E = 2.119e5;
sigma_y = 690;

Q = 0.5*P*sqrt((B/2)^2+x(2)^2/x(2));
sigma = Q/(pi*T*x(1));
g(1) = sigma - sigma_y;
sigma_c = 0.125*pi^2*E*(x(1)^2+T^2)/((B/2)^2+x(2)^2);
g(2) = sigma - sigma_c;
g(3) = 200 -x(2);
g(4) = x(1) -140;
g(5) = 20 - x(1);
g(6) = x(2) - 1200;
ceq = [];

