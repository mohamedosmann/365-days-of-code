import heapq

def shortest_path(satellites, start, target):
    # Priority queue (min-heap) for the shortest path
    priority_queue = [(0, start)]  # (distance, satellite)
    
    # Store the shortest known distances
    shortest_distances = {sat: float('inf') for sat in satellites}
    shortest_distances[start] = 0
    
    # Store the shortest path
    previous_nodes = {sat: None for sat in satellites}

    while priority_queue:
        current_distance, current_sat = heapq.heappop(priority_queue)

        # Stop if we reach the target
        if current_sat == target:
            break

        for neighbor, weight in satellites[current_sat].items():
            distance = current_distance + weight

            # If found a shorter path, update and push to priority queue
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                previous_nodes[neighbor] = current_sat
                heapq.heappush(priority_queue, (distance, neighbor))

    # Reconstruct the shortest path
    path = []
    sat = target
    while sat:
        path.insert(0, sat)
        sat = previous_nodes[sat]

    return shortest_distances[target], path

# Example Test
satellites = {
    'S1': {'S2': 10, 'S3': 20},
    'S2': {'S1': 10, 'S3': 5, 'S4': 30},
    'S3': {'S1': 20, 'S2': 5, 'S4': 5},
    'S4': {'S2': 30, 'S3': 5, 'S5': 15},
    'S5': {'S4': 15}
}

start = 'S1'
target = 'S5'

min_delay, best_route = shortest_path(satellites, start, target)
print("🚀 Minimum Communication Delay:", min_delay, "ms")
print("🛰️ Best Route:", " → ".join(best_route))
