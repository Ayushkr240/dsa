
# def tsp(cost , curr , visited , count , total , path):
#     global ans , best_path
#     n= len(cost)

#     # checking if all cities have been visited
#     if count ==n:
#         total+=cost[curr][0]

#         # checkif the total cost is less than the ans then update ans
#         if total<ans:
#             ans=total
#             best_path=path+[0]
#         return 

#     for i in range(n):
#         if i not in visited:
#             new_cost= total + cost[curr][i]

#             if new_cost<ans:
#                 visited.add(i)

#                 # now exploring other nodes from i using recursion
#                 tsp(cost,i,visited,count+1,new_cost,path+[i])
#                 visited.remove(i)


def tsp(cost , curr , visited , total , count , path):
    global best_path , ans
    n= len(cost)

    if count == n :
        total+= cost[curr][0]

        if total<ans:
            ans=total
            best_path=path+[0]
        return

    for i in range(n):
        if i not in visited:
            new_cost=total+cost[curr][i]

            if new_cost<ans:
                visited.add(i)

                tsp( cost , i , visited , new_cost , count +1 , path + [i])
                visited.remove(i)


# Cost of travelling between cities
cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

ans = float('inf')  # Initially, minimum cost is infinity
best_path = []      # Store the best route

# Start from city 0 with no travel cost


tsp(cost,0, {0},0,1,[0])

# Display the minimum cost and optimal route
print("Minimum cost:", ans)
print("Best path:", " -> ".join(map(str, best_path)))