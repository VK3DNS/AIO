import sys
sys.setrecursionlimit(1000000000)

N = 0

K = 0

costs = []

# Open the input and output files.
input_file = open("shopin.txt", "r")
output_file = open("shopout.txt", "w")

input_line = input_file.readline().strip()
N, K = map(int, input_line.split())
print(N, K)
input_line = input_file.readline().strip()
costs = list(map(int, input_line.split()))

totalCost = 0

def orderCosts():
    costs.sort()
    return costs

costs = orderCosts()

for i in range(K):
    print('a')
    cheapest = costs[0]
    costs = costs[1:-1]

    totalCost += cheapest

for i in range(len(costs)//2):
    totalCost += costs[-1]
    costs = costs[:-2]

answer = totalCost

output_file.write("%d\n" % (answer))

input_file.close()
output_file.close()
