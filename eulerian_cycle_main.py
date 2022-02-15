# finding cycles and merging it with each other for final path
import sys

sys.stdin = open('test.txt', 'r')
line = sys.stdin.readline

def new_cycle_search() -> int:
    global cycle_ind
    for index, cycle in enumerate(path):
        for point in cycle:
            if graph[point]: # finds the connection point
                path.append([point]) # starts new cycle
                cycle_ind += 1 # ... same as command above
                join.append([*sorted([index, cycle_ind]), point]) # adds a connection information
                return point
    return 0 # if didnt find the connection point indirectly ends programm

def path_build() -> list:
    global join
    join = sorted(join, reverse=True) # sort all connection data in reversed order
    for data in join:
        c1, c2, point = data # unpack connection data
        insert = path[c1].index(point) # finds connection point in first cycle
        path[c1].pop(insert) # prepears first cycle for connection
        for num in path[c2]: # connects second cycle to first
            path[c1].insert(insert, num)
    return path[0]

v, e = [int(i) for i in line().split()] # builds graph
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    fr, to = [int(i) for i in line().split()]
    graph[fr].append(to)
    graph[to].append(fr)

path = [[1]] # path storage (with cycles before path_build())
cycle_ind = 0 # cycle count (used like index for path)
join = [] # the point when cycles connects with each other (cycle1, cycle2, connection point)

des = 1 # comes to start point

while True:
    cur = graph[des] # current list of available desdinations
    if not cur: # stop the cycle when no available directions
        is_cycle = path[-1][-1] == path[-1][0] and len(path[-1]) > 1
        if not is_cycle: # ... and this 'cycle' is not a cycle
            print('NONE')
            break
        no_ribs = all([True if i == [] else False for i in graph])
        if no_ribs: # ... and no ribs exist
            print(*path_build()[:-1])
            break
        else: # ... and there are ribs exist
            des = new_cycle_search() # find entry point for new cycle search
            continue 
    now = des # store current point
    des = cur[0] # choose new desdination point
    cur.remove(des) # remove rib from graph
    graph[des].remove(now) # ... same as command above
    path[cycle_ind].append(des) # add point to path