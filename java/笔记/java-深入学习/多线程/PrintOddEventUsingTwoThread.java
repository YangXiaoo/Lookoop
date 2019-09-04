import java.util.*;

// 两个线程交替打印奇数与偶数
public class PrintOddEventUsingTwoThread {
	private static Object lock = new Object();
	private static int start = 0;

	public static void main(String[] args) {
		Runnable task1 = new Runnable() {
			@Override
			public void run() {
				while (start <= 100) {
					synchronized (lock) {
						System.out.println(start);
						start += 1;
						lock.notifyAll();
						try {
							lock.wait();
						} catch (Exception e) {
							e.printStackTrace();
						}
					}					
				}
			}
		};

		Runnable task2 = new Runnable() {
			@Override
			public void run() {
				while (start <= 99) {
					synchronized (lock) {
						System.out.println(start);
						start += 1;
						lock.notifyAll();
						try {
							lock.wait();
						} catch (InterruptedException e) {
							e.printStackTrace();
						}
					}					
				}
			}
		};

		try {
			new Thread(task1).start();	// 先打印偶数
			Thread.sleep(100);
			new Thread(task2).start();	// 打印奇数			
		} catch (InterruptedException e) {
			e.printStackTrace();
		}

	}
}