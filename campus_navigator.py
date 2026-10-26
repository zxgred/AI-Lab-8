    
campus = {
    "Hostel": {
        "Cafeteria": 150,
        "Admin Block": 300,
        "Sports Complex": 180
    },
    "Cafeteria": {
        "Academic Block": 200
    },
    "Admin Block": {
        "Academic Block": 120
    },
    "Academic Block": {
        "Library": 100,
        "Sports Complex": 160
    },
    "Sports Complex": {
        "Academic Block": 160
    },
    "Library": {}
}

heuristic = {
    "Hostel": 350,
    "Cafeteria": 260,
    "Admin Block": 150,
    "Academic Block": 90,
    "Sports Complex": 200,
    "Library": 0
}


def gbfs(start, goal):
    frontier = [(heuristic[start], start, [start], 0)]
    visited = []

    while frontier:
        frontier.sort()
        h, current, path, cost = frontier.pop(0)

        if current in visited:
            continue

        visited.append(current)

        if current == goal:
            print("Path found by GBFS:", path)
            print("Total cost of this path:", cost)
            return

        for neighbor, distance in campus[current].items():
            if neighbor not in visited:
                frontier.append((
                    heuristic[neighbor],
                    neighbor,
                    path + [neighbor],
                    cost + distance
                ))

    print("No path found")


gbfs("Hostel", "Library")


