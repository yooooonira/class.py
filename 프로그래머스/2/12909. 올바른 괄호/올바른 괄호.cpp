#include<string>
#include <iostream>

using namespace std;

bool solution(string s){
    int count =0;

    for (int i=0;i<s.size(); i++){
        if (s[i]=='('){
            count +=1;
        } else{
            count-=1;
        }

        if (count<0){
            return false;
        }
    }

    return count == 0;

}

// (가 나오면 
// 맨 뒤에서 )를 찾아서 이 둘을 삭제하거나 바로 뒤에서 )를 찾아서 삭제하거나. 

/*
접근을 '삭제'로 잡으면 복잡해짐. 이 문제는 스택/카운트로 푸는게 정석. 

( 나오면 +1
) 나오면 -1

중간에 count가 음수면 false
끝났을때 count가 0이면 true


*/