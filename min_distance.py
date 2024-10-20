# Problem: Find Minimum Distance (Double Loop)
a = [1, 5, 11, -1, 2]
min_distance = float('inf')
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        distance = abs(a[i] - a[j])
        if distance < min_distance:
            min_distance = distance
print(min_distance)
