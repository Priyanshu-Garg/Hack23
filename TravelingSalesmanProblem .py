import itertools
import math

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def total_distance(path, points):
    distance = 0
    for i in range(len(path) - 1):
        distance += calculate_distance(points[path[i]], points[path[i + 1]])
    distance += calculate_distance(points[path[-1]], points[path[0]])  # Return to the starting point
    return distance

def brute_force_tsp(points):
    n = len(points)
    min_distance = float("inf")
    min_path = None

    for perm in itertools.permutations(range(n)):
        distance = total_distance(perm, points)
        if distance < min_distance:
            min_distance = distance
            min_path = perm

    return min_path, min_distance

if __name__ == "__main__":
    # Example points (replace with your own)
    points = [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]

    shortest_path, shortest_distance = brute_force_tsp(points)
    print("Shortest Path:", shortest_path)
    print("Shortest Distance:", shortest_distance)
