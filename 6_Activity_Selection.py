"""# Always select the activity that finishes earliest among the activities you can still choose.
def activitySelection(start, finish):
    n = len(start)

    activities = sorted(zip(start, finish), key=lambda x: x[1])

    selected = [activities[0]]
    last_finish = activities[0][1]

    for i in range(1, n):
        if activities[i][0] >= last_finish:
            selected.append(activities[i])
            last_finish = activities[i][1]

    return selected

# activitise = [ (1,2) , (3,4) , (0,6) , (5,7) , (8,9) , (5,9) ]
start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

result = activitySelection(start, finish)

print("Selected activities:", result)
print("Maximum number of activities:", len(result))"""

def selected_activity(start,finish):
    n=len(start)

    activities= sorted(zip(start,finish), key=lambda x:x[1])
    selected=[activities[0]]
    last_time=activities[0][1]

    for i in range(1,n):
        if activities[i][0]>=last_time:
            selected.append(activities[i])
            last_time=activities[i][0]

    return selected

start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

result = selected_activity(start, finish)

print("Selected activities:", result)
print("Maximum number of activities:", len(result))