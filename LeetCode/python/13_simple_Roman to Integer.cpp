class Solution {
public:
    int romanToInt(string s) {
        map<char, int> mapper;
        mapper.insert(pair<char, int>('I', 1));
        mapper.insert(pair<char, int>('V', 5));
        mapper.insert(pair<char, int>('X', 10));
        mapper.insert(pair<char, int>('L', 50));
        mapper.insert(pair<char, int>('C', 100));
        mapper.insert(pair<char, int>('D', 500));
        mapper.insert(pair<char, int>('M', 1000));
        
        int ret = 0;
        int pre = 1;
        for (int i = s.size() - 1; i >= 0; --i) {
            map<char, int>::iterator it = mapper.find(s[i]); 
            int curValue = it->second;
            if (curValue >= pre) {
                ret += curValue;
            } else {
                ret -= curValue;
            }
            pre = curValue;
        }
        
        return ret;
    }
};