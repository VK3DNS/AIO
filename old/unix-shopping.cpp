#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

int main() {
    std::ifstream input_file("shopin.txt");
    std::ofstream output_file("shopout.txt");

    int N, K;
    input_file >> N >> K;

    std::vector<int> costs(N);
    for (int i = 0; i < N; ++i) {
        input_file >> costs[i];
    }

    int totalCost = 0;

    for (int i = 0; i < K; i++) {
        if (costs.size() < 2) {
            break;
        }
        int cheapest = costs[0];
        costs.erase(costs.begin());
        costs.pop_back();
        totalCost += cheapest;
    }

    for (int i = 0; i < costs.size() / 2; i++) {
        if (costs.size() < 2) {
            break;
        }
        totalCost += costs.back();
        costs.pop_back();
        costs.pop_back();
    }

    output_file << totalCost << std::endl;

    input_file.close();
    output_file.close();

    return 0;
}