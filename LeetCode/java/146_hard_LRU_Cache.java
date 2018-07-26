/**
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */
/*
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
 */

// 2018-7-26
// 146. LRU Cache
// LRU(Least Recently Used)
// http://flychao88.iteye.com/blog/1977653
/**
对于LRU cache，往往会有以下要求：
1. 假设Cache里面的 entry 都是按照序列保存的，那么，对于新的entry，我们把它放置在最前面。
2. 如果一个entry已经存在，我们再次访问到该entry的时候，我们需要把它放在cache的最前面。
3. 当cache满了的时候，需要把最后一个entry 从cache里面移除出去，然后再往里插入 entry。
 */
// LTE
class 146_hard_LRU_Cache {
    private int capacity;
    private HashMap<Integer, Node> cache;
    private DoubleLink  visited;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<Integer, Node>();
        this.visited = new DoubleLink();
    }
    
    public int get(int key) {
        if (this.cache.containsKey(key)) {
            Node node = this.cache.get(key);
            this.visited.setHead(node);
            return node.value;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if (this.cache.containsKey(key)) {
            Node node = this.cache.get(key);
            node.value = value;
            this.visited.setHead(node);
        } else {
            if (this.visited.size >= this.capacity) {
                Node node_tail = this.visited.tail;
                this.visited.remove(node_tail);
                this.cache.remove(node_tail.key);
            }
            Node node = new Node(key, value);
            this.visited.insert(node);
            this.cache.put(key, node);
        }
    }

    private class Node {
        int key;
        int value;
        Node pre;
        Node next;

        public Node(int key, int value) {
            this.key = key;
            this.value = value;
            this.pre = null;
            this.next = null;
        }
    }
    // Define DoublLink
    private class DoubleLink {
        Node head;
        Node tail;
        int size;

        public DoubleLink() {
            this.head = null;
            this.tail = null;
            this.size = 0;
        }

        public void insert(Node node) {
            node.next = this.head;
            if (this.head != null) {
                this.head.pre = node;
            } else {
                this.tail = node;
            }

            this.head = node;
            this.size++;
        }

        public void setHead(Node node) {
            Node node_pre = node.pre;
            Node node_next = node.next;

            if (node_pre != null) {
                node_pre.next = node_next;
                if (node_next != null) {
                    node_next.pre = node_pre;
                } else {
                    this.tail = node_next;
                }

                node.next = this.head;
                this.head.pre = node;
                node.pre = null;
                this.head = node;
            }
        }
        public void remove(Node node) {
            Node node_pre = node.pre;
            Node node_next = node.next;

            if (node_pre != null) {
                node_pre.next = node_next;
            } else {
                this.head = node_pre;
            }

            if (node_next != null) {
                node_next.pre = node_pre;
            } else {
                this.tail = node_next;
            }
            this.size--;
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */