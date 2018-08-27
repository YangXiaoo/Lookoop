/* 
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary(旅程) in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical( 词汇的) order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code International Air Transport Association 机场代码, 三字码).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
*/

// 2018-8-27
// 332. Reconstruct Itinerary
// 遍历有向图的每一条边，且不重复, 欧拉图
// https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C++
#include <stdio.h>
class Solution {
public:
    map<string, multiset<string>> targets;
    vector<string> route;

    vector<string> findItinerary(vector<pair<string, string>> tickets) {
        for (auto ticket : tickets)
            targets[ticket.first].insert(ticket.second);
        visit("JFK");
        return vector<string>(route.rbegin(), route.rend());
    }
    void visit(string airport)
    {
        while (targets[airport].size())
        {
            string next = *targets[airport].begin(); // .begin()为 指针
            targets[airport].erase(targets[airport].begin());
            visit(next);
        }

        route.push_back(airport); // 递归从栈里弹出时是倒序的，最后结果要翻转
    }
};

int main()
{
    vector<vector<string>> ticket = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    vector<pair<string,string>> tickets;
    vector<vector<string>>::iterator T;
    vector<string> res;

    vector<string>::iterator it;
    for(T=ticket.begin();T<ticket.end();T++)
    {
        for (it=(*T).begin();it<(*T).end();it++)
        {
            tickets.insert(pair(*((*T).begin()), *((*T).end())));
        }

    Solution test;
    res = test.findItinerary(tickets);
    for (vector<string>::iterator it=res.begin(); it != res.end; it++)
        cout << *it << endl;
}