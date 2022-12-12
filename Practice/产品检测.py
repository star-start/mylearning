# 为了解决这个问题，我们可以使用滑动窗口的方法。我们可以遍历整个产品序列，维护一个M从序列开头滑动到结尾的大小窗口。对于每个窗口，我们可以计算窗口中产品的“优秀”标准的数量，并跟踪所有窗口中优秀标准的最小数量。

# 此代码遍历M产品序列中大小为 size 的所有窗口，计算每个窗口的优秀标准的数量并跟踪优秀标准的最小数量。
# n要使用此代码，您可以在第一行输入、m和 的值k，然后在后续行中输入产品序列。输出将是所有窗口中优秀标准的最少数量。

# Find the minimum number of excellent criteria among all windows of size M
def find_min_excellent_criteria(n, m, k, products):
  min_excellent_criteria = float('inf')

  # Iterate over the windows
  for i in range(n - m + 1):
    # Compute the number of excellent criteria for the current window
    excellent_criteria = 0
    for j in range(i, i + m):
      excellent_criteria += products[j].count('1')

    # Update the minimum number of excellent criteria
    min_excellent_criteria = min(min_excellent_criteria, excellent_criteria)

  return min_excellent_criteria

# Read input
n, m, k = map(int, input().split())
products = [input() for _ in range(n)]

# Find the minimum number of excellent criteria among all windows
min_excellent_criteria = find_min_excellent_criteria(n, m, k, products)

# Print the result
print(min_excellent_criteria)
