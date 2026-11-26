# DSA - Greedy Program 01: Activity Selection

def select_activities(activities):
    # Sort activities by finish time
    activities = sorted(activities, key=lambda activity: activity[1])

    selected = []
    last_finish = float("-inf")

    for start, finish in activities:

        # Pick the activity if it does not overlap
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish

    return selected


# (start time, finish time)
activities = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]

result = select_activities(activities)

print("Selected Activities:", result)
print("Maximum Activities:", len(result))
