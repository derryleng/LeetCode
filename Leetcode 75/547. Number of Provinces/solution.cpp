// There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

// A province is a group of directly or indirectly connected cities and no other cities outside of the group.

// You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

// Return the total number of provinces.

class Solution {
public:
    void dfs(int i, vector<vector<int>>& isConnected, vector<int>& visited) {
        visited[i] = 1;
        for (int j = 0; j < isConnected[i].size(); j++) {
            if (isConnected[i][j] == 1 && visited[j] == 0) {
                dfs(j, isConnected, visited);
            }
        }
    }

    int findCircleNum(vector<vector<int>>& isConnected) {
        int counter = 0;
        int n = isConnected.size();
        vector<int> visited(n, 0);
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                counter++;
                dfs(i, isConnected, visited);
            }
        }
        return counter;
    }
};
