import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
// 2019/9/4

// 使用静态方法
public class ProductConsumer {
	private static final int MAX_SIZE = 100;
	private static final int FULL_SIZE = 10;
	private static int curSzie = 0;
	private static ReentrantLock lock = new ReentrantLock();
	private static Condition condition = lock.newCondition();

	public static void main(String[] args) {
		Runnable product = new Runnable() {
			public void run() {
				for (int i = 0; i < MAX_SIZE; ++i) {
					lock.lock();
					try {
						while (FULL_SIZE == curSzie) {
							condition.await();
						}
						++curSzie;
						System.out.println("curSzie: " + curSzie);
						condition.signal();
						Thread.sleep(10);
					} catch (Exception e) {
						e.printStackTrace();
					} finally {
						lock.unlock();
					}
					
				}

			}
		};

		Runnable consume = new Runnable() {
			public void run() {
				for (int i = 0; i < MAX_SIZE; ++i) {
					lock.lock();
					try {
						while (curSzie == 0) {
							condition.await();
						}
						--curSzie;
						System.out.println("curSzie: " + curSzie);
						condition.signal();
						Thread.sleep(10);
					} catch (InterruptedException e) {
						e.printStackTrace();
					} finally {
						lock.unlock();
					}
				}
			}
		};

		new Thread(product).start();
		new Thread(consume).start();

	}
}

