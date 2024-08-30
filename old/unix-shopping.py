import sys
sys.setrecursionlimit(1000000000)

input_file = open("shopin.txt", "r")
output_file = open("shopout.txt", "w")

input_line = input_file.readline().strip()
N, K = map(int, input_line.split())
input_line = input_file.readline().strip()
costs = list(map(int, input_line.split()))
totalCost = 0

for i in range(K):
    if len(costs) < 2:
        break
    cheapest = costs[0]
    print(cheapest)
    costs = costs[1:-1]
    totalCost += cheapest

for i in range(len(costs)//2):
    if len(costs) < 2:
        break
    print(totalCost)
    totalCost += costs[-1]
    costs = costs[:-2]

answer = totalCost

output_file.write("%d\n" % (answer))

input_file.close()
output_file.close()