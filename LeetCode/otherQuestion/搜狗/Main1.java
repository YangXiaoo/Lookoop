import java.util.*;
import java.io.*;


class SelfMap {
	int capacity;
	HashMap<String, Node> cache;
	DoubleLink visited;

	public SelfMap(int capacity) {
		this.capacity = capacity;
		this.cache = new HashMap<>();
		this.visited = new DoubleLink();
	}

	public void put(String key, String val) {
		if (this.cache.containsKey(key)) {	// 如果包含该节点则更新
			Node node = this.cache.get(key); // 获得该节点
			node.val = val;	// 跟新
			this.visited.setHead(node);
		} else {
			if (this.visited.size >= this.capacity) {	// 淘汰旧记录并打印
				Node nodeTail = this.visited.tail;
				this.visited.remove(nodeTail);
				this.cache.remove(nodeTail.key);
				System.out.println(nodeTail.key + " " + nodeTail.val);
			}

			Node node = new Node(key, val);
			this.visited.insert(node);
			this.cache.put(key, node);
		}
	}
}


class Node {
	String key, val;
	Node pre, next;

	public Node(String key, String val) {
		this.key = key;
		this.val = val;
		this.pre = null;
		this.next = null;
	}
}

class DoubleLink {
	Node head, tail;
	int size;

	public DoubleLink() {
		this.head = null;
		this.tail = null;
		this.size = 0;
	}

	public void insert(Node node) {
		node.next = this.head;	// 插入到头结点
		if (this.head != null) {
			this.head.pre = node;
		} else {
			this.tail = node;
		}

		this.head = node;	// 更新头结点
		this.size++;
	}

	public void setHead(Node node) {
		Node pre = node.pre, next = node.next;
		if (pre != null) {	// 连接前驱节点与后节点
			pre.next = next;
			if (next != null) {
				next.pre = pre;
			} else {
				this.tail = pre;
			}

			// 更新头结点
			node.next = this.head;
			this.head.pre = node;
			node.pre = null;
			this.head = node;
		}
	}

	public void remove(Node node) {
		Node pre = node.pre, next = node.next;
		if (pre != null) {
			pre.next = next;
		} else {
			this.head = next;
		}

		if (next != null) {
			next.pre = pre;
		} else {
			this.tail = pre;
		}

		this.size--;
	}
}
public class Main1 {
	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in);
		int capacity = Integer.parseInt(cin.nextLine());
		SelfMap map = new SelfMap(capacity);
		while (cin.hasNext()) {
			String line = cin.nextLine();
			// System.out.println(line);
			String[] s = line.split(" ");
			// System.out.println(Arrays.toString(s));
			map.put(s[0], s[1]);
		}
	}
}

/*
2
10_123_50_A0 1566918054
10_123_50_A1 1566918054
10_123_50_A1 1566918055
10_123_50_A3 1566918055
10_123_50_A4 1566918056
*/