from itertools import combinations
import math

def antenna_coords(grid, freq):
    for ri, r in enumerate(grid):
        for ci, c in enumerate(r):
            if c == freq: yield ri, ci

def antinode_coords(antenna_coords, grid, repeat = False):
    for A, B in combinations(antenna_coords, 2):
        dr = B[0] - A[0]
        dc = B[1] - A[1]

        # It turns out that there are not antennas in the data that require this normalization
        GCD = math.gcd(dr, dc)
        dr //= GCD
        dc //= GCD

        i = 0 if repeat else 1
        while True:
            C = B[0]+i*dr, B[1]+i*dc
            if not coord_in_grid(C, grid): break
            yield C
            if not repeat: break
            i += 1
        i = 0 if repeat else 1
        while True:
            C = A[0]-i*dr, A[1]-i*dc 
            if not coord_in_grid(C, grid): break
            yield C
            if not repeat: break
            i += 1
    
def coord_in_grid(coord, grid): return 0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid[0])

def number_of_antinodes(grid, repeat):
    c = set()
    freqs = set([c for row in grid for c in row if c != '.'])
    for freq in freqs:
        for coord in antinode_coords(antenna_coords(grid, freq), grid, repeat):
            if coord_in_grid(coord, grid):
                c.add(coord)
    return len(c)

def solve(data):
    with open(data) as f:
        grid = [list(row.strip()) for row in f.readlines()]
    
    yield number_of_antinodes(grid, repeat=False)
    yield number_of_antinodes(grid, repeat=True)