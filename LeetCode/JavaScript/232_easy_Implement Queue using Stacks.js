/**
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
**/

// 232. Implement Queue using Stacks [Easy]
// 2019/10/21

/**
 * Initialize your data structure here.
 */
var MyQueue = function() {
    this.stack1 = [];	// 入栈
    this.stack2 = [];	// 出栈
};

/**
 * Push element x to the back of queue. 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
    this.stack1.push(x);
};

/**
 * Removes the element from in front of queue and returns that element.
 * @return {number}
 */
MyQueue.prototype.pop = function() {
    if (this.stack2.length == 0) {
        while (this.stack1.length != 0) {
            this.stack2.push(this.stack1.pop());
        }
    }
    
    if (this.stack2.length == 0) {
        return -1;
    }
    
    return this.stack2.pop();
};

/**
 * Get the front element.
 * @return {number}
 */
MyQueue.prototype.peek = function() {
    if (this.stack2.length == 0) {
        while (this.stack1.length != 0) {
            this.stack2.push(this.stack1.pop());
        }
    }
    return this.stack2[this.stack2.length - 1];
};

/**
 * Returns whether the queue is empty.
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
    return (this.stack1.length + this.stack2.length) == 0;
};

/** 
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */

var queue = new MyQueue();

queue.push(1);
queue.push(2);  
console.log(queue.peek());  // returns 1
console.log(queue.pop());   // returns 1
console.log(queue.empty()); // returns false