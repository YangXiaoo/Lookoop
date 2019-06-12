// 2019-5-11
// AOP 动态代理
// https://www.cnblogs.com/lcngu/p/5339555.html
import java.util.*;

import java.lang.reflect.Proxy;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;


interface IHello {
	void say(String str);	// 接口不能实现
}

class Hello implements IHello {
	@Override
	public void say(String str) {
		System.out.println("hello say: " + str);
	}
}

interface ILogger {
	void start(Method method);
	void end(Method method);
}

class Logger implements ILogger {
	@Override
	public void start(Method method) {
		System.out.println(new Date() + " - " + method.getName() + "  start.");
	}

	@Override
	public void end(Method method) {
		System.out.println(new Date() + " - " + method.getName() + "  end.");
	}
}

class DynamicProxyHello implements InvocationHandler {
	private Object target;
	private Object proxy;

	// 绑定该类实现的所有接口, 取得代理类
	public Object bind(Object target, Object proxy) {
		this.target = target;
		this.proxy = proxy;

    	// public static Object newProxyInstance(ClassLoader loader, 
     	//                                        Class<?>[] interfaces, 
     	//                                        InvocationHandler h)
		return Proxy.newProxyInstance(this.target.getClass().getClassLoader(),
									  this.target.getClass().getInterfaces(), this);
	}

	@Override
	public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
		Object ret = null;

		// 反射得到操作者的实例
		Class inst = this.proxy.getClass();

		// 获得 void satrt(Method method)
		// https://www.cnblogs.com/xinhuaxuan/p/6019531.html
		Method start = inst.getDeclaredMethod("start", new Class[]{Method.class});
		// 反射执行start方法
		// Method类的invoke(Object obj,Object args[])方法接收的参数必须为对象
		start.invoke(this.proxy, new Object[]{method});

		// 执行要处理对象的原本方法
		method.invoke(this.target, args);

		// 反射执行end
		Method end = inst.getDeclaredMethod("end", new Class[]{Method.class});
		end.invoke(this.proxy, new Object[]{method});

		return ret;
	}
}

public class main {
	public static void main(String[] args) {
		IHello hello = (IHello) new DynamicProxyHello().bind(new Hello(), new Logger());
		hello.say("test successful!");
	}
}

// Sat May 11 18:37:41 CST 2019 - say  start.
// hello say: test successful!
// Sat May 11 18:37:41 CST 2019 - say  end.