import sys
sys.setrecursionlimit(1000000000)

with open('backin.txt', 'r') as input_file:
    N, K = map(int, input_file.readline().strip().split())
    D = list(map(int, input_file.readline().strip().split()))
    C = list(map(int, input_file.readline().strip().split()))

current_town = 0
total_cost = 0
num_cans = 0


for i in range(N - 1):
    cans_needed = D[i]

    if num_cans < cans_needed:
        cans_to_buy = cans_needed - num_cans
        total_cost += cans_to_buy * C[current_town]
        num_cans += cans_to_buy

    num_cans -= cans_needed
    current_town += 1

with open('backout.txt', 'w') as output_file:
    output_file.write(f"{total_cost }\n")