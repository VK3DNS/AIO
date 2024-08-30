#include <iostream>
#include <fstream>
#include <vector>

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
    int left = 0;
    int right = N - 1;

    for (int i = 0; i < K; ++i) {
        if (right - left + 1 < 2) {
            break;
        }
        int cheapest = costs[left];
        left++;
        right--;
        totalCost += cheapest;
    }

    int halfSize = (right - left + 1) / 2;
    for (int i = 0; i < halfSize; ++i) {
        if (right - left + 1 < 2) {
            break;
        }
        totalCost += costs[right];
        right--;
        if (right - left + 1 >= 2) {
            right--;
        }
    }

    output_file << totalCost << std::endl;

    input_file.close();
    output_file.close();

    return 0;
}