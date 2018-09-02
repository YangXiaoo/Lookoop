# class Solution {
# public:
#     struct comparator{
#       bool operator()(const vector<int>& v1, const vector<int>& v2) {
#           return v1[1] < v2[1];
#       } 
#     };
    
#     /** Main Function ***/
#     int scheduleCourse(vector<vector<int>>& courses) 
#     {
#         sort(courses.begin(), courses.end(), comparator());
        
#         // Priority Queue by default sorted in MAX HEAP ORDER
#         priority_queue<int> q;
        
#         int sum = 0;
#         for (auto& c : courses)
#         {
#             int t = c[0]; //Course time
#             int d = c[1]; //Max day before which course has to be completed
            
#             q.push(t);
#             sum += t;
            
#             if (sum > d)
#             {
#                 sum -= q.top(); //This can be some other long course
#                 q.pop();
#             }

#         }
#         return q.size();
#     }
# };



# import queue

# class Solution(object):
#     """docstring for Solution"""
#     def scheduleCourse(self, courses):
#         courses.sort(key = lambda x: x[1])
#         maxCourses, currentV, currentUse = 0, 0, 0
#         maxQueue = queue.PriorityQueue()
#         for course in courses:
#             currentV = course[1]
#             if currentUse + course[0] <= currentV:
#                 maxCourses += 1
#                 currentUse += course[0]
#                 maxQueue.put((-course[0], course[0]))
#             else:
#                 currentMax = maxQueue.get()[1]
#                 if currentMax > course[0]:
#                     currentUse = currentUse - currentMax + course[0]
#                     maxQueue.put((-course[0], course[0]))
#                 else:
#                     maxQueue.put((-currentMax, currentMax))
#         return maxCourses

import queue

p = queue.PriorityQueue()
p.put(1)
p.put(15)
p.put(3)
print(p.pop())