import java.util.*;
import java.util.concurrent.*;

// 执行线程，按顺序打印数字
public class excuteThreadByOrder {
	private static final int MAX_THREADS = 10;
	public static void main(String[] args) {

		ExecutorService pool = Executors.newSingleThreadExecutor();

		for (int i = 0; i < MAX_THREADS; ++i) {
			final int order = i;
			Runnable task = () -> {
				try {
					System.out.println(order);
				} catch (Exception e) {
					e.printStackTrace();
				}
				
			};
			pool.execute(task);
		}
	}
}