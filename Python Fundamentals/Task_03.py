import heapq

def ucs_cheapest_route(graph, start, goal):
    pq = [(0, [start])]
    visited = set()
    explored_count = 0

    print("--- Exploring Partial Paths in UCS Order ---")
    while pq:
        cost, path = heapq.heappop(pq)
        node = path[-1]
        
        explored_count += 1
        print(f"Expanding path: {path} with total cost: {cost}")
        
        if node == goal:
            print("--------------------------------------------")
            return path, cost, explored_count
        
        if node in visited:
            continue
            
        visited.add(node)
        
        for neighbor, ticket_price in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + ticket_price, path + [neighbor]))

    print("--------------------------------------------")
    return None, None, explored_count

if __name__ == "__main__":
    flights = {
        "Islamabad": [("Lahore", 40), ("Karachi", 90)],
        "Lahore": [("Karachi", 50), ("Peshawar", 30)],
        "Karachi": [("Quetta", 60)],
        "Peshawar": [("Quetta", 70)],
        "Quetta": [],
    }

    cheapest_route, total_cost, count = ucs_cheapest_route(flights, "Islamabad", "Quetta")

    if cheapest_route:
        print(f"Cheapest route: {cheapest_route}")
        print(f"Total ticket cost: {total_cost}")
        print(f"Total routes explored: {count}")
    else:
        print("No route found.")