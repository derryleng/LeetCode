// There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

// When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

// Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

class Solution {
public:
    void visitRoom(int i, vector<vector<int>>& rooms, vector<bool>& visited) {
        visited[i] = true;
        // cout << "Visited " << i << endl;
        for (int key = 0; key < rooms[i].size(); key++) {
            if (!visited[rooms[i][key]]) {
                visitRoom(rooms[i][key], rooms, visited);
            }
        }
    }

    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        vector<bool> visited(n, false);
        visitRoom(0, rooms, visited);
        // for (bool elem : visited) {
        //     cout << elem << " ";
        // }
        return none_of(cbegin(visited), cend(visited), logical_not<bool>());
    }
};
