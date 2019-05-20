// 多线程笔记.java

1.中断线程
	void interrupt() 	// 向线程发送中断请求，线程的中断状态被设置为true
						// 如果目前该线程被一个sleep调用阻塞，那么InterrunptedExce-
						// ption异常被抛出。
	static boolean interrupted()	// 测试当前线程是否被中断。它将当前线程的中断状态
									// 置为false。
	boolean isInterrupted()			//测试线程是否被中断，不会改变中断状态。
	static Thread currentThread()	// 返回代表当前线程的Thread对象。

2. 线程状态
	NEW
	RUNNABLE 
	BLOCKING
	WAITING 
	TIMED_WAITING 
	TERMINATED
	// Thread方法
	void join();
	void join(long millis);
	Thread.State.getState(); // 返回当前线程状态。

3. 线程属性
	// 1-线程优先级
	void setPriority(int newPriority);	// 设置线程优先级，必须在MIN_PRIORITY与
										// MAX_PRIORITY之间。
										// 一般使用Thread.NORM_PRIORITY优先级。
										// static int MIN_PRIORITY
										// static int NORM_PRIORITY
										// static int MAX_PRIORITY

	static void yield();	// 导致当前线程处于让步状态。如果其他可运行线程具有至少
							// 与此线程同样高的优先级，那么这些线程接下来会被调度。
	// 2-守护线程
	t.setDaemon(true);	// 为其他线程提供服务，当只剩下守护线程时虚拟机退出。
						// 必须在线程启动之前调用，永远不要访问固有资源，因
						// 为它会在任何时刻发生中断。
	// 3-未捕获异常处理器
	// 暂无

4. 同步
	// 1-锁对象
	private Lock mylock = new ReentrantLock();	// ReentrantLock(boolean fair), 
												// 带有公平策略的锁 ，偏爱等待时间
												// 最长的线程，但大大降低性能，所以
												// 锁没有被强制为公平。
	public void foo() {
		mylock.lock();
		try {
			// critical section
		}
		finally {
			mylock.unlock();
		}
	}


	// 2-条件对象, 条件锁
	// 使用方法
	private Lock mylock = new ReentrantLock();
	private Condition mycondition = mylock.newCondition();	// 创建条件锁,管理那些
															// 已经获得锁的对象但
															// 不能做有用功的线程。 
	private static int threadhold = 100;
	private int curValue;
	public void foo() {
		mylock.lock();
		try {
			while (curValue > threadhold ) 
				mycondition.await();	// 进入该条件的等待集, 等待条件对象发出解除
										// 阻塞通知。 与等待获得锁的线程有本质区别, 
										// 当锁可用时, 不能立刻解除阻塞状态，必须要
										// 等待另一线程调用相同条件上的signalAll()。
			// critical section
			// do something
			mycondition.signalAll();	// signalAll不会立即激活一个等待线程, 而是
										// 解除等待线程的阻塞, 当当前线程退出同步方
										// 法后, 通过竞争实现对对象的访问。
			// 另一种通知方法
			// mycondition.signalAll();	// siganl随机解除等待集中某个线程的阻塞状态,
										// 若被解除阻塞状态线程不能运行, 如果没有被
										// 其余线程调用signal, 则会形成死锁。
		}
		finally {
			mylock.unlock();
		}
	}


	// 3-synchronized, 内部锁
	// 使用方法
	private static int threadhold = 100;
	private int curValue;
	public synchronized void foo() {
		try {
			while (curValue > threadhold ) 
				wait();	// wait(long millis);
						// wait(long millis, int nanos);

			// critical section
			// do something
			notifyAll();	// notify();
		}
	}

	// 4-同步阻塞, 客户端锁定
	synchronized (obj) {	// obj 为一个被同步修改对象, 可以为this
		// critical section
	}

	// 5-volatile域
	// 原方法
	private boolean done;
	public synchronized boolean isDone() { return done; }
	public synchronized void setDone() { done = true; }

	// volatile为实例域的同步访问提供一种免锁机制, 上述代码可以进行如下更改
	private volatile boolean done;
	public boolean isDone() { return done; }
	void setDone() { done = true; }


	// 6-final
	// 可以初始化一个域使得所有线程都能访问更新后的值
	final Map<String, Double> map = new HashMap<>();	// 其他线程会在构造函数完成
														// 之后才能看到map值。然而
														// 并不是线程安全的，如果多
														// 个线程读写这个表仍需要进
														// 行同步。
	
	// 7-原子性
	public static AtomicLong largest = new AtomicLong();
	// Java SE 8 中更新largest
	largest.updateAndGet(x -> Math.max(x, observed));
	largest.accumulateAndGet(observed, Math::max);

	// 8-死锁
	// need do something

	// 9-线程局部变量
	// ThreadLocal 适用于每个线程需要自己独立的实例且该实例需要在多个方法中被使用, 
	// 即变量在线程间隔离而在方法或类间共享的场景

	// 问题原型
	public static final SimpleDateFormat dateFormat = 
		new SimpleDateFormat("yyyy-MM-dd");

	String dateStamp = dateFormat.format(new Date);	// 不是线程安全

	// 解决办法
	public static final ThreadLocal<SimpleDateFormat> dateFormat = 
		ThreadLocal.withInitial(() -> new SimpleDateFormat("yyyy-MM-dd"));
	String dateStamp = dateFormat.get().format(new Date);	// 使用

	// 另一种初始化
	private static ThreadLocal<StringBuilder> counter = 
		new ThreadLocal<StringBuilder>() {
      	@Override
      	protected StringBuilder initialValue() {
        	return new StringBuilder();
      	}
    };
    String counterToString = counter.get().toString();

    // 10-锁测试与超时
    // lock方法不能被中断,而带有超时参数的tryLock，如果在等待期间被中断，将抛出
    // InterruptedException异常, 允许程序打破死锁。
    if (mylock.tryLock(100, TimeUnit.MILLISECONDS)) {	// 成功返回true, 失败返回
    	try { ... }										// false。
    	final { mylock.unlock(); }
    } else {
    	// do something
    }

    // 11-读/写锁
    private ReentrantReadWriteLock wrl = new ReentrantReadWriteLock();
    private Lock readLock = wrl.readLock();
    private Lock writeLock = wrl.writeLock();

5. 阻塞队列
	// 见代码

6. 线程安全的集合

7. Callable与Future
	// 见代码

8. 执行器  
	ExecutorService的生命周期包括了：运行关闭和终止三种状态。
 	1) newSingleThreadExecutor()
		public class excuteThreadByOrder {
			private static final int MAX_THREADS = 10;
			public static void main(String[] args) {

				ExecutorService executor = Executors.newSingleThreadExecutor();

				for (int i = 0; i < MAX_THREADS; ++i) {
					final int order = i;
					Runnable task = () -> {
						try {
							System.out.println(order);
						} catch (Exception e) {
							e.printStackTrace();
						}
						
					};
					executor.execute(task);
				}
			}
		}
	2) ExecutorService executor = Executors.newCachedThreadPool();
	3) ExecutorService executor = Executors.newFixedThreadPool(10);
	
	// executor.submit(Callable) // 参数为继承Callable并实现call的实例
    ExecutorService pool = Executors.newCachedThreadPool();
    Matcher matcher = new Matcher(new File(directory), keyword, pool);	// 继承Callable并实现call
    Future<List<File>> result = pool.submit(matcher);

9. 线程安全与不安全
	// 线程不安全
	ArrayList
	LinkedList
	HashMap
	HashSet
	TreeMap
	TreeSet
	StringBulider
	// 线程安全
	Vector 
	HashTable
	StringBuffer

	// 使用同步包装器实现线程安全, 但还是需要同步方法
	List<T> synchArrayList = Collections.synchronizedList(new ArrayList<T>());
	Map<K, V> synchMap = Collections.synchronizedMap(new HashMap<K, V>());

	// java.util.concurrent提供的线程安全集合
	ConcurrentHashMap
	ConcurrentSkipListMap
	ConcurrentSkipListSet
	ConcurrentLinkedQueue