public class StartState implements State {
	// 创建实现接口的类
	public void doAction(Context context) {
		System.out.println("Player is in start state");
		context.setState(this);
	}
	public String toString(){
		return "Start State";
	}
};