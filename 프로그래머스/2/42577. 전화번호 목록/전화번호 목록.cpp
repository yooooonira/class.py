#include <string>
#include <vector>

#include <algorithm>


using namespace std;

bool solution(vector<string> phone_book) {
    sort(phone_book.begin(), phone_book.end());
    //정렬을 하니까 인접한것만 비교해도 무방
    
    for (int i =0;i <phone_book.size()-1;i++){
        if(phone_book[i]==phone_book[i+1].substr(0,phone_book[i].size())){
            return false;
        }
    }
    return true;
    
}

