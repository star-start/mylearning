# # Read the input
# k = int(input())
#
# # Create a list to store the initial positions and number of robots at each position
# positions = []
#
# # Read the initial positions and number of robots
# for i in range(k):
#     n, x, y = map(int, input().split())
#     positions.append((n, x, y))
#
# # Initialize the minimum total energy to a large value
# min_total_energy = float("inf")
#
# # Loop over all possible meeting points
# for i in range(1, k+1):
#     for j in range(1, n+1):
#         # Compute the total energy consumed by all the robots at this meeting point
#         total_energy = 0
#         for x, y, n in positions:
#             total_energy += abs(i - x) + abs(j - y) # Compute the distance from the meeting point to the initial position
#         # Update the minimum total energy if necessary
#         min_total_energy = min(min_total_energy, total_energy)
#
# # Print the minimum total energy
# print(min_total_energy)

# Compute the distances between all robots using a breadth-first search
# def compute_distances(m, n, robots):
#   distances = [[float('inf')] * len(robots) for _ in range(len(robots))]
#   for i, (x, y, n) in enumerate(robots):
#     visited = [[False] * n for _ in range(m)]
#     q = [(x, y, 0)]
#     visited[x][y] = True
#     while q:
#       x, y, d = q.pop(0)
#       for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
#           if (nx, ny) in [(x, y) for x, y, _ in robots]:
#             j = [idx for idx, (x, y, _) in enumerate(robots) if (x, y) == (nx, ny)][0]
#             distances[i][j] = distances[j][i] = d + 1
#           visited[nx][ny] = True
#           q.append((nx, ny, d + 1))
#   return distances
#
# # Find the optimal gathering point for the robots
# def find_optimal_gathering_point(m, n, robots):
#   # Compute the distances between all robots
#   distances = compute_distances(m, n, robots)
#
#   # Find the robot that minimizes the sum of distances to all other robots
#   min_distance = float('inf')
#   for i in range(len(robots)):
#     distance = sum(distances[i])
#     if distance < min_distance:
#       min_distance = distance
#       min_robot = i
#
#   return min_robot, min_distance
#
# # Read input
# k = int(input())
# robots = []
# for _ in range(k):
#   x, y, n = map(int, input().split())
#   robots.append((x, y, n))
#
# # Find the optimal gathering point for the robots
# min_robot, min_distance = find_optimal_gathering_point(k, n, robots)
#
# # Print the result
# print(min_distance)


# 多个机器人分布在M*N(10≤M,N≤1000)的方格中，每个机器人分布在不同的方格里。规定每个机器人只能向上下左右的相邻方格移动，每移动一个方格需要消耗1个单位能量。
# 现在要求所有机器人集合，集合点只能是某个机器人初始所在方格。
# 现在请找一个集合点，使得所有机器人到达该点消耗的总能量最低。
# 输入说明：
# 第一行是一个整数K（0<K≤100），表示机器人的总数。
# 之后K行是每个机器人所在方格的位置，用x，y表示，以空格隔开。
# 输出说明：
# 输出最低的总能量消耗。
# 输入样例：
# 4
# 4 5
# 3 3
# 2 2
# 4 4

# 输出样例：7
k=int(input())
robots = []
for i in range(k):
    x, y = map(int, input().split())
    robots.append((x, y))
min_energy = float('inf')
for x, y in robots:
    energy = 0
    for xx, yy in robots:
        energy += abs(xx - x) + abs(yy - y)
    min_energy = min(min_energy, energy)
print(min_energy)
