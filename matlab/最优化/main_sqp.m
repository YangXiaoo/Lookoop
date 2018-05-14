%sqp方法主函数
%x0为初始点
x0=[4 4]';
mu0=[ ]';
lam0=[0 0 0 0]';
[x,mu,lam,val,k]=sqpm(x0,mu0,lam0)
v=f1(x);
disp('	********** 人字架尺寸优化设计最优解 ********** 	');
fprintf('	钢管平均直径 	D = %3.4f mm\n',x(1))
fprintf('	  人字架高度	    H = %3.4f mm\n',x(2))
fprintf('	  人字架体积	    V = %3.4f mm^3\n',v)