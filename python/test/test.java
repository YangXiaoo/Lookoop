package test;
import test.Context;
public class test {
	// 使用context类来查看状态state改变的状态
	public static void main(String[] args) {
		Context context = new Context();
		StartState startState = new StartState();
		startState.doAction(context);
		System.out.println(context.getState().toString());
		StopState stopState = new StopState();
		stopState.doAction(context);
		System.out.println(context.getState().toString());
	}
}