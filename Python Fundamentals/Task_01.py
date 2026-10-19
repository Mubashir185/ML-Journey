def bfs_shortest_path(graph, start, goal):
    if start == goal:
        return [start]
    queue = [[start]]
    visited = {start}
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        for neighbor in graph.get(node, []):
            if neighbor == goal:
                return path + [neighbor]
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
                
    return None

if __name__ == "__main__":
    network = {
        "Ali": ["Bilal", "Sara"],
        "Bilal": ["Ali", "Zara"],
        "Sara": ["Ali", "Omar"],
        "Zara": ["Bilal", "Hira"],
        "Omar": ["Sara"],
        "Hira": ["Zara"],
    }

    shortest_chain = bfs_shortest_path(network, "Ali", "Hira")

    if shortest_chain:
        print(f"Shortest chain from Ali to Hira: {shortest_chain}")
        print(f"Number of introductions needed: {len(shortest_chain) - 1}")
    else:
        print("No connection found.")