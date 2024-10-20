# Problem: Find Minimum Distance (Alternative using a set for faster lookups)
a = [1, 5, 11, -1, 2]
min_distance = float('inf')
visited = set()

for num in a:
    for v in visited:
        distance = abs(num - v)
        if distance < min_distance:
            min_distance = distance
    visited.add(num)

print(min_distance)
