#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    //최종 정답 저장. (몇 개씩 배포되는지.)
    vector<int> days;
    //각 기능이 완료되기까지 걸리는 날짜를 저장. ex) [3,1,9]

    for(int i =0;i<progresses.size(); i++){ //모든 기능을 순회
        int remain = 100-progresses[i];  //100까지 얼마나 남았는지 계산 
        int day = (remain + speeds[i] -1)/speeds[i]; //완료까지 필요한 날짜 계산 (올림 나눗셈)
        days.push_back(day); //그 계산을 저장 
    }

    int current = days[0];  //현재 배포 기준 날짜. 즉 첫 기능[0]이 완료되는 날짜. 
    int count =1;           //현재 배포 묶음 개수. 첫 기능 포함하니까 1부터 시작. 

    for (int i=1; i<days.size(); i++){ //두번째 기능부터 순회. 
        if(days[i]<=current){          //현재 기준 날짜 안에 i번째 기능이 완료되면. 
            count++;                   //배포 묶음 개수++
        }else{                         //현재 기준 날짜 안에 i번째 기능이 완료되지 않으면. 
            answer.push_back(count);   //완료되지 않은대로 묶음을 정답에 추가 
            current=days[i];           //새 배포기준으로 갱신 
            count =1;                  //마찬가지로 갱신 
        }
    }
    answer.push_back(count);           //마지막 배포 붂은 저장. 
    return answer;                     //최종 반환 

}
