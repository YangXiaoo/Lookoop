/**
抽象类只能被继承
继承接口必须重写方法
**/
public abstract class Game {
	abstract void initialize();
	abstract void startPlay();
	abstract void endPlay();

	// 模板
	// final关键字修饰类表示不能被继承
	// final修饰方法表示方法不能被重写
	// final修饰成员变量表示该变量必须初始化并且只初始化一次
	public final void play(){
		// 初始化游戏
		initialize();
		// 开始游戏
		startPlay();
		// 结束游戏
		endPlay();
	}
}

public class Cricket extends Game {
	@Override
	void endPlay() {
		System.out.println("Cricket Game Finished!");
	}
	@Override
	void initialize() {
		System.out.println("Cricket Game Initialized! Start playing.");
	}
	@Override
	void startPlay() {
		System.out.println("Cricket Game Started. Enjoy the game!");
	}
}


public class Football extends Game {
	@Override
	void endPlay() {
		System.out.println("Football Game Finished!");
	}
	@Override
	void initialize() {
		System.out.println("Football Game Initialized! Start playing.");
	}
	@Override
	void startPlay() {
		System.out.println("Football Game Started. Enjoy the game!");
	}
}


public class TemplatePatternDemo {
	public static void main(String[] args) {
	Game game = new Cricket();
	game.play();
	System.out.println();
	game = new Football();
	game.play();
	}
}

/*
输出结果：
	Cricket Game Initialized! Start playing.
	Cricket Game Started. Enjoy the game!
	Cricket Game Finished!

	Football Game Initialized! Start playing.
	Football Game Started. Enjoy the game!
	Football Game Finished!
*/