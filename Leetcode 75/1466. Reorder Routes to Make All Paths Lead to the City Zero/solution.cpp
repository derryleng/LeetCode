// There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

// Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

// This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

// Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

// It's guaranteed that each city can reach city 0 after reorder.

class Solution {
public:
    void dfs(int node, unordered_map<int, list<pair<int, bool>>>& graph, vector<bool>& visited, int& counter) {
        visited[node] = true;
        for (pair neighbour : graph[node]) {
            int dest = neighbour.first; // Path destination
            bool reversed = neighbour.second; // Reversed path
            if (!visited[dest]) {
                if (reversed) {
                    counter++;
                }
                dfs(dest, graph, visited, counter);
            }
        }
    }

    int minReorder(int n, vector<vector<int>>& connections) {
        // Represent connections in adjacency list
        unordered_map<int, list<pair<int, bool>>> graph;
        for (const vector<int>& k : connections) {
            graph[k[0]].push_back({k[1], 1}); // Real path
            graph[k[1]].push_back({k[0], 0}); // Reversed path
        }

        vector<bool> visited(n, false);
        int counter = 0;
        dfs(0, graph, visited, counter);
        return counter;
    }
};
