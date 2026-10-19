def dfs_can_reach(maze, start, exit_room, visited=None):
    if visited is None:
        visited = []   
    if start not in visited:
        visited.append(start)    
    if start == exit_room:
        return True, visited
    for neighbor in maze.get(start, []):
        if neighbor not in visited:
            reached, visited = dfs_can_reach(maze, neighbor, exit_room, visited)
            if reached:
                return True, visited
                
    return False, visited

if __name__ == "__main__":
    maze = {
        "Entrance": ["Hall1", "Hall2"],
        "Hall1": ["Room1"],
        "Hall2": ["Room2", "Trap"],
        "Room1": [],
        "Room2": ["Exit"],
        "Trap": [],
        "Exit": [],
    }

    can_reach, visit_order = dfs_can_reach(maze, "Entrance", "Exit")

    print(f"Visit order: {visit_order}")
    print(f"Can reach Exit from Entrance? {can_reach}")