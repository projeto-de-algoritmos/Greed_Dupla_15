class Solution {
   public:
    int maxArea(vector<int>& height) {
        int start = 0;
        int end = height.size() - 1;
        int max_area = 0;

        while (start < end) {
            int current_area = (end - start) * min(height[start], height[end]);
            max_area = max(max_area, current_area);

            if (height[start] <= height[end])
                start += 1;
            else
                end -= 1;
        }

        return max_area;
    }
};