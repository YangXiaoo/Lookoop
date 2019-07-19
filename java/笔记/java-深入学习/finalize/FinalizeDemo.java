// finalize()方法使用
// 不推荐使用原因： (1)调用时机不确定性;(2)并不一定能保证执行
public class FinalizeDemo {
	public static FinalizeDemo gcObj = null;

	@Override
	protected void finalize() throws Throwable {
		super.finalize();
		gcObj = this;
		System.out.println("gc-finalize");
	}

	public static void main(String[] args) throws Throwable {
		gcObj = new FinalizeDemo();
		gcObj = null;
		System.gc();
		Thread.sleep(500);

		if (gcObj != null) {
			System.out.println("exist");
		}
	}
}