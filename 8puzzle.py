import time
from queue import Queue
from queue import LifoQueue as Stack

game = '041763852'
goal = '012345678'


def move_up(l, i):
    l[i], l[i - 3] = l[i - 3], l[i]


def move_down(l, i):
    l[i], l[i + 3] = l[i + 3], l[i]


def move_right(l, i):
    l[i], l[i + 1] = l[i + 1], l[i]


def move_left(l, i):
    l[i], l[i - 1] = l[i - 1], l[i]


def get_neighbors(l):
    n = []
    i = l.index('0')
    if i not in [0, 1, 2]:
        x1 = l.copy()
        move_up(x1, i)
        n.append(x1)
    if i not in [6, 7, 8]:
        x1 = l.copy()
        move_down(x1, i)
        n.append(x1)
    if i not in [2, 5, 8]:
        x1 = l.copy()
        move_right(x1, i)
        n.append(x1)
    if i not in [0, 3, 6]:
        x1 = l.copy()
        move_left(x1, i)
        n.append(x1)
    return n


def BFS(board):
    done = False
    # algorithm
    start_time = time.time()
    start = board
    frontier = Queue()
    frontier_set = set()
    frontier.put(start)
    frontier_set.add(start)
    explored = set()
    parent = {start: start}
    while not frontier.empty():
        s = frontier.get()
        frontier_set.pop()
        explored.add(s)
        if s == goal:
            done = True
            break
        neighbors = get_neighbors(list(s))
        for n in neighbors:
            n = "".join(n)
            if (n not in explored) and (n not in frontier_set):
                frontier.put(n)
                frontier_set.add(n)
                parent[n] = s
    finish_time = time.time()
    if not done:
        print("game unsolvable!")
        return False
    # path tracking and analysis
    key = goal
    steps = [key]
    while key in parent.keys():
        t = key
        steps.append(parent[key])
        key = parent[key]
        del parent[t]
    steps.pop(-1)  # start state was added to the parent map with itself as value
    steps.reverse()
    print("\n## BFS ##")
    print(f"explored nodes: {len(explored)}")
    print(f"run time: {finish_time - start_time}s")
    print(f"cost of path: {len(steps) - 1}")
    print("--------------------------------------------")
    print("\nsteps:\n")
    for i in list(steps):
        print(i)
    print("\n###############################################\n")


def DFS(board):
    done = False
    # algorithm
    start_time = time.time()
    start = board
    frontier = Stack()
    frontier_set = set()
    frontier.put(start)
    frontier_set.add(start)
    explored = set()
    parent = {start: start}
    while not frontier.empty():
        s = frontier.get()
        frontier_set.pop()
        explored.add(s)
        if s == goal:
            done = True
            break
        neighbors = get_neighbors(list(s))
        for n in neighbors:
            n = "".join(n)
            if (n not in explored) and (n not in frontier_set):
                frontier.put(n)
                frontier_set.add(n)
                parent[n] = s
    finish_time = time.time()
    if not done:
        print("game unsolvable!")
        return False
    # path tracking and analysis
    key = goal
    steps = [key]
    while key in parent.keys():
        t = key
        steps.append(parent[key])
        key = parent[key]
        del parent[t]
    steps.pop(-1)  # start state was added to the parent map with itself as value
    steps.reverse()
    print("\n## DFS ##")
    print(f"explored nodes: {len(explored)}")
    print(f"run time: {finish_time - start_time}s")
    print(f"cost of path: {len(steps) - 1}")
    print("--------------------------------------------")
    print("\nsteps:\n")
    for i in list(steps):
        print(i)
    print("\n###############################################\n")

BFS(game)
DFS(game)
