/* 
******************     水塘抽样(Reservoir Sampling)问题    ******************
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();
*/
// ================================================================
/*
首先考虑k为1的情况，即：给定一个长度很大或者长度未知数据流，限定对每个元素只能访问一次，写出一个随机选择算法，使得所有元素被选中的概率相等。

设当前读取的是第n个元素，采用归纳法分析如下：

n = 1 时，只有一个元素，直接返回即可，概率为1。
n = 2 时，需要等概率返回前两个元素，显然概率为1/2。可以生成一个0～1之间的随机数p，p < 0.5 时返回第一个，否则返回第二个。
n = 3 时，要求每个元素返回的概率为1/3。注意此时前两个元素留下来的概率均为1/2。做法是：生成一个0～1之间的随机数，若<1/3，则返回第三个，否则返回上一步留下的那个。元素1和2留下的概率均为：1/2 * (1 - 1/3) = 1/3，即上一步留下的概率乘以这一步留下（即元素3不留下）的概率。
假设 n = m 时，前n个元素留下的概率均为：1/n = 1/m；
那么 n = m+1 时，生成0～1之间的随机数并判断是否<1/(m+1)，若是则留下元素m+1，否则留下上一步留下的元素。这样一来，元素m+1留下的概率为1/(m+1)，前m个元素留下来的概率均为：1/m * (1 - 1/(m+1)) = 1/(m+1)，也就是1/n。
综上可知，算法成立。
 

问题二
将问题一中的条件变为，k为任意整数的情况，即要求最终返回的元素有k个，这就是水塘抽样（Reservoir Sampling）问题。要求是：取到第n个元素时，前n个元素被留下的几率相等，即k/n。

算法同上面思路类似，将1/n换乘k/n即可。在取第n个数据的时候，我们生成一个0到1的随机数p，如果p小于k/n，替换池中任意一个为第n个数。大于k/n，继续保留前面的数。直到数据流结束，返回此k个数。但是为了保证计算机计算分数额准确性，一般是生成一个0到n的随机数，跟k相比，道理是一样的。

同样采用归纳法来分析：

初始情况 n <= k：此时每个元素留下的概率均为1。
当 n = k+1 时，第k+1个元素留下的概率为k/(k+1)，前k个元素留下的概率均为：k/k * (1 - k/(k+1) * 1/k) = k/(k+1)，即上一步留下的概率乘以这一步留下的概率。
假设 n = m 时，每个元素留下的概率均为 k/n = k/m。
那么，当 n = m+1 时，第m+1个元素留下的概率为1/(m+1)，前m个元素留下的概率均为：k/m * (1 - k/(m+1) * 1/k) = k/(m+1)，其中：k/m为上一步留下来的概率，k/(m+1) * 1/k 为这一步不能留下来的概率（第m+1个留下来，同时池中一个元素被踢出的概率）。
综上可知，算法成立。


假设数据序列的规模为 n，需要采样的数量的为 k。
首先构建一个可容纳 k 个元素的数组，将序列的前 k 个元素放入数组中。
然后从第 k+1 个元素开始，以 k/n 的概率来决定该元素是否被替换到数组中（数组中的元素被替换的概率是相同的）。 当遍历完所有元素之后，数组中剩下的元素即为所需采取的样本。
//stream代表数据流
//reservoir代表返回长度为k的池塘
//从stream中取前k个放入reservoir；
for ( int i = 1; i < k; i++)
    reservoir[i] = stream[i];
for (i = k; stream != null; i++) {
    p = random(0, i);
    if (p < k) reservoir[p] = stream[i];
return reservoir;
===================================================================
*/
// 2018-8-28
// 382. Linked List Random Node
// https://leetcode.com/problems/linked-list-random-node/description/
// https://www.cnblogs.com/strugglion/p/6424874.html

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

// using std::default_random_engine;
// std::uniform_int_distribution<int>

class Solution {
private:
	ListNode* head;
public:
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* head) {
        this->head = head;
    }
    
    /** Returns a random node's value. */
    int getRandom() {
		int res = head->val;
		ListNode* node = head->next;
		int i = 2;
		while (node)
		{
			int j = rand() % i;
			if (j == 0)
				res = node->val;
			i++;
			node = node->next;
		}       
		return res;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */