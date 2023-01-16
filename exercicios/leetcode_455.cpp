// 455. Assign Cookies

class Solution {
   public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());

        int ans = 0, s_pointer = 0;
        for (int i = 0; i < g.size(); i++) {
            for (int j = s_pointer; j < s.size(); j++) {
                if (g[i] <= s[j]) {
                    ans++;
                    s_pointer = j + 1;
                    break;
                }
            }
        }

        return ans;
    }
};