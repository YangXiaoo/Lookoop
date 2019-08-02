'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

# 2018-11-23
# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# https://www.cnblogs.com/lightwindy/p/8674041.html 有四种方法
"""
1. 字典-桶排序
2. 大堆
3. TreeMap
4. 快排-先set

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dicts = {}
        for i in nums:
            dicts[i] = dicts.get(i, 0) + 1
        print(dicts)
        sort = sorted(dicts.items(),key = lambda x:x[1],reverse = True)
        res = []
        for i in range(k):
            res.append(sort[i][0])
        return res

# Java Heap
# class Pair{
#     int num;
#     int count;
#     public Pair(int num, int count){
#         this.num=num;
#         this.count=count;
#     }
# }
  
# public class Solution {
#     public List<Integer> topKFrequent(int[] nums, int k) {
#         //count the frequency for each element
#         HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
#         for(int num: nums){
#             if(map.containsKey(num)){
#                 map.put(num, map.get(num)+1);
#             }else{
#                 map.put(num, 1);
#             }
#         }
  
#         // create a min heap
#         PriorityQueue<Pair> queue = new PriorityQueue<Pair>(new Comparator<Pair>(){
#             public int compare(Pair a, Pair b){
#                 return a.count-b.count;
#             }
#         });
  
#         //maintain a heap of size k.
#         for(Map.Entry<Integer, Integer> entry: map.entrySet()){
#             Pair p = new Pair(entry.getKey(), entry.getValue());
#             queue.offer(p);
#             if(queue.size()>k){
#                 queue.poll();
#             }
#         }
  
#         //get all elements from the heap
#         List<Integer> result = new ArrayList<Integer>();
#         while(queue.size()>0){
#             result.add(queue.poll().num);
#         }
#         //reverse the order
#         Collections.reverse(result);
  
#         return result;
#     }
# }




# Java TreeMap       
# public class Solution {
#     public List<Integer> topKFrequent(int[] nums, int k) {
#         Map<Integer, Integer> map = new HashMap<>();
#         for(int n: nums){
#             map.put(n, map.getOrDefault(n,0)+1);
#         }
         
#         TreeMap<Integer, List<Integer>> freqMap = new TreeMap<>();
#         for(int num : map.keySet()){
#            int freq = map.get(num);
#            if(!freqMap.containsKey(freq)){
#                freqMap.put(freq, new LinkedList<>());
#            }
#            freqMap.get(freq).add(num);
#         }
         
#         List<Integer> res = new ArrayList<>();
#         while(res.size()<k){
#             Map.Entry<Integer, List<Integer>> entry = freqMap.pollLastEntry();
#             res.addAll(entry.getValue());
#         }
#         return res;
#     }
# }　
nums = [1]
k = 1
test = Solution()
res = test.topKFrequent(nums, k)
print(res)


        