#include <string>
#include <vector>

#include <algorithm>

using namespace std;

/*
경쟁자가 참여자에 없으면 반환. 
*/
string solution(vector<string> participant, vector<string> completion) {
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());

    for (int i = 0; i < completion.size(); i++) {
        if (participant[i] != completion[i]) {
            return participant[i];
        }
    }

    return participant[participant.size() - 1];
}