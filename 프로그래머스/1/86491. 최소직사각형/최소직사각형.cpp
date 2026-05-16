#include <string>
#include <vector>

#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int maxW=0;
    int maxH=0;
    
    for (int i=0;i<sizes.size();i++){
        int W =max(sizes[i][0], sizes[i][1]);
        int H =min(sizes[i][0], sizes[i][1]);
        
        maxW=max(maxW,W);
        maxH=max(maxH,H);
        
    }
    
    return maxW*maxH;
        
        
}

// 모든 명함을 “긴 쪽 = 가로”, “짧은 쪽 = 세로”로 통일
    
