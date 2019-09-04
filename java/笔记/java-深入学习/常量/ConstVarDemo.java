import java.util.*;

// 2019/9/4
public class ConstVarDemo {
	private final int v1 = 1;
	private static final int v2 = 2;

	private final List<Integer> list1 = new LinkedList<>();
	private static final List<Integer> list2 = new LinkedList<>();


	// 基本类型常量修改
	// 编译失败
	public void test1() {
		// System.out.println(v1);

		// 以下操作错误: 无法为最终变量v1分配值
		// v1 = 11;	// 修改常量的值

		// System.out.println(v1);


		// System.out.println(v2);

		// 以下操作错误: 无法为最终变量v2分配值
		// v2 = 22;	// 修改静态常量的值
		// System.out.println(v2);	
	}

	// 对象引用常量状态进行修改
	// 编译通过
	public void test2() {
		System.out.println(list1.toString());
		list1.add(1);	// 常量引用
		System.out.println(list1.toString());

		System.out.println(list2.toString());
		list2.add(2);	// 静态常量引用
		System.out.println(list2.toString());
	}
	
	// 改变对象类型常量的引用
	// 编译失败
	public void test3() {
		// System.out.println(list1.toString());
		// list1 = new ArrayList<>();	// 错误: 无法为最终变量list1分配值
		// list1.add(1);
		// System.out.println(list1.toString());

		// System.out.println(list2.toString());
		// list2 = new ArrayList<>();	// 错误: 无法为最终变量list2分配值
		// list2.add(2);
		// System.out.println(list2.toString());
	}

	public static void main(String[] args) {
		new ConstVarDemo().test3();
	}
}