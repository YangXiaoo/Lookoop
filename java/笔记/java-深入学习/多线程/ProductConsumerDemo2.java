import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

// 2019/9/4
// 成员类实现
public class ProductConsumerDemo2 {
	private int count = 0;
	private static final int MAX_SIZE = 10;
	private Lock lock = new ReentrantLock();
	private Condition cond = lock.newCondition();

	class Product implements Runnable {
		public void run() {
			while (true) {
				lock.lock();
				try {
					while (count == MAX_SIZE) {
						cond.await();
					}
					count++;
					System.out.println("count: " + count);
					cond.signalAll();
					Thread.sleep(10);
				} catch (InterruptedException e) {
					// pass
				}finally {
					lock.unlock();
				}
			}
		}
	}

	class Consume implements Runnable {
		public void run() {
			while (true) {
				lock.lock();
				try {
					while (count == 0) {
						cond.await();
					}
					count--;
					System.out.println("count: " + count);
					cond.signalAll();
					Thread.sleep(10);
				} catch(InterruptedException e) {
					// pass
				} finally {
					lock.unlock();
				}
			}
		}
	}

	public static void main(String[] args) {
		ProductConsumerDemo2 demo = new ProductConsumerDemo2();
		new Thread(demo.new Product()).start();
		new Thread(demo.new Consume()).start();
	}
}