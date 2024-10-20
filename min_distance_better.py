# Problem: More Efficient Minimum Distance (Sort Approach)
a = [1, 5, 11, -1, 2]
a.sort()
min_distance = float('inf')
for i in range(len(a) - 1):
    distance = abs(a[i] - a[i + 1])
    if distance < min_distance:
        min_distance = distance
print(min_distance)
