#include <string>
#include <vector>

#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    int time =0;
    int currentWeight=0;
    
    int nextTruck = 0;

    queue<int> bridge;

    for (int i = 0; i < bridge_length; i++) {
        bridge.push(0);
    }

    while (!bridge.empty()) {
        time++;

        currentWeight -= bridge.front();
        bridge.pop();

        if (nextTruck < truck_weights.size()) {
            if (currentWeight + truck_weights[nextTruck] <= weight) {
                bridge.push(truck_weights[nextTruck]);
                currentWeight += truck_weights[nextTruck];
                nextTruck++;
            } else {
                bridge.push(0);
            }
        }
    }

    return time;
}



    
    