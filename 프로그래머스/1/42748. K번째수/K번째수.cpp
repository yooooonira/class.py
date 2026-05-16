#include <string>
#include <vector>

#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> result;

    for (int i =0;i<commands.size(); i++){
        int start = commands[i][0]-1;
        int end = commands[i][1];
        int k = commands[i][2]-1;
        
        vector<int> temp(array.begin()+start, array.begin()+end);
        //temp라는 int형 배열 생성
        sort(temp.begin(), temp.end());
        
        result.push_back(temp[k]);
    }
    return result;
}

// 배열 array의 i번째 숫자부터 j번재 숫자까지 자르고, 정렬했을때, k번째에 있는 수를 구하려고 한다. 
//     예를 들어 [1, (5, 2, 6, 3), 7, 4]  i = 2, j = 5, k = 3이라면
//     정렬하면 [2,3,5,6] k번째 수는 5 
    