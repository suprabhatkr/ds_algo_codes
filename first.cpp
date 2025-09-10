#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<vector<int>> arr(n, vector<int>(n));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            cin >> arr[i][j];

    vector<double> centrality(n, 0.0);
    double maxCentrality = 0.0;
    for (int src = 0; src < n; ++src) {
        vector<int> dist(n, -1);
        queue<int> q;
        dist[src] = 0;
        q.push(src);
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v = 0; v < n; ++v) {
                if (arr[u][v] && dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.push(v);
                }
            }
        }
        int sum = 0;
        for (int i = 0; i < n; ++i) {
            if (i != src) sum += dist[i];
        }
        if (sum > 0) centrality[src] = 1.0 / sum;
        if (centrality[src] > maxCentrality) maxCentrality = centrality[src];
    }

    vector<int> result;
    for (int i = 0; i < n; ++i) {
        if (abs(centrality[i] - maxCentrality) < 1e-9) result.push_back(i);
    }
    sort(result.begin(), result.end());
    for (int i = 0; i < result.size(); ++i) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}

