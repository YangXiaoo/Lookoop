public class Context {
	// 创建context类
	private State state;
	public Context(){
		state = null;
	}
	public void setState(State state){
		this.state = state;
	}
	public State getState(){
		return state;
	}
};