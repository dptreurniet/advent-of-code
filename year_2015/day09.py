
# This solution uses an implementation of the Travelling Salesman Problem found here: https://www.geeksforgeeks.org/travelling-salesman-problem-using-dynamic-programming/
# In this implementation, all cities are visited once, but the salesman also return to the starting city.
# The AoC problem does not require the return, so a modification is needed.
# A dummy city is added with distance 0 to every other city, which transforms the Travelling Salesman Problem into the right form.

# Python program to find the shortest possible route
# that visits every city exactly once and returns to
# the starting point using memoization and bitmasking

import sys
def totalCost(mask, pos, n, cost):
  
    # Base case: if all cities are visited, return the
    # cost to return to the starting city (0)
    if mask == (1 << n) - 1:
        return cost[pos][0]

    ans = sys.maxsize   

    # Try visiting every city that has not been visited yet
    for i in range(n):
        if (mask & (1 << i)) == 0: 
  
            # If city i is not visited, visit it and 
             #  update the mask
            ans = min(ans, cost[pos][i] +
                      totalCost(mask | (1 << i), i, n, cost))

    return ans
 

def tsp(cost):
    n = len(cost)
    
    # Start from city 0, and only city 0 is visited 
    # initially (mask = 1)
    return totalCost(1, 0, n, cost)
 

def solve(data):
    with open(data) as f:
        lines = [line.strip() for line in f.readlines()]
    
    places = []
    for line in lines:
        places.extend(line.split()[0:3:2])
    places = list(set(places))
    
    cost = [[0 for _ in range(len(places)+1)] for _ in range(len(places)+1)]
    for line in lines:
        line_split = line.split()
        A, B = [places.index(p) for p in line_split[0:3:2]]
        cost[A][B] = int(line_split[-1])
        cost[B][A] = int(line_split[-1])

    yield tsp(cost)

    # Part 2

    yield -1 * tsp([[-c for c in line] for line in cost])

