#include <vector>

#include <set>

using namespace std;

int solution(vector<int> nums)
{
    set<int> s(nums.begin(), nums.end());

    int maxPick = nums.size() / 2;

    if (s.size() < maxPick) {
        return s.size();
    }

    return maxPick;
}