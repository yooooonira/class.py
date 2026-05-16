#include <vector>
#include <iostream>


using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> result;
    
    for (int i=0;i<arr.size();i++){
        if (result.empty() || result.back()!=arr[i]){
            result.push_back(arr[i]);
        }
    }
    return result;
}


// set은 중복제거하면서 정렬도 되기 때문에 사용 x