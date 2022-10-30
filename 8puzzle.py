import time
from queue import Queue
from queue import LifoQueue as Stack
from queue import PriorityQueue as Heap
import math

game = '436215087'
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
    frontier.put((start, 0))
    frontier_set.add(start)
    explored = set()
    parent = {start: start}
    max_depth = 0

    while not frontier.empty():
        s, depth = frontier.get()
        max_depth = max(max_depth, depth)
        frontier_set.pop()
        explored.add(s)
        if s == goal:
            done = True
            break
        neighbors = get_neighbors(list(s))
        for n in neighbors:
            n = "".join(n)
            if (n not in explored) and (n not in frontier_set):
                frontier.put((n, depth + 1))
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
    print("\nsteps:\n")
    for i in list(steps):
        print(i)
    print("--------------------------------------------")
    print(f"expanded nodes: {len(explored)}")
    print(f"run time: {finish_time - start_time}s")
    print(f"cost of path: {len(steps) - 1}")
    print(f"search depth: {max_depth}")
    print("\n###############################################\n")


def DFS(board):
    done = False

    # algorithm
    start_time = time.time()
    start = board
    frontier = Stack()
    frontier_set = set()
    frontier.put((start, 0))
    frontier_set.add(start)
    explored = set()
    parent = {start: start}
    max_depth = 0

    while not frontier.empty():
        s, depth = frontier.get()
        max_depth = max(max_depth, depth)
        frontier_set.remove(s)
        explored.add(s)
        if s == goal:
            done = True
            break
        neighbors = get_neighbors(list(s))
        for n in neighbors:
            n = "".join(n)
            if (n not in explored) and (n not in frontier_set):
                frontier.put((n, depth + 1))
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
    print("\nsteps:\n")
    for i in list(steps):
        print(i)
    print("--------------------------------------------")
    print(f"expanded nodes: {len(explored)}")
    print(f"run time: {finish_time - start_time}s")
    print(f"cost of path: {len(steps) - 1}")
    print(f"search depth: {max_depth}")
    print("\n###############################################\n")


def A_star(board, h):
    done = False

    # algorithm
    start_time = time.time()
    start = board
    frontier = Heap()
    frontier_set = {}
    frontier.put((h(start), start, 0))
    frontier_set[start] = 0
    explored = set()
    parent = {start: start}
    max_depth = 0

    while not frontier.empty():
        fs, s, depth = frontier.get()
        if s in explored:
            continue
        max_depth = max(max_depth, depth)
        frontier_set.pop(s)
        explored.add(s)
        if s == goal:
            done = True
            break
        neighbors = get_neighbors(list(s))
        for n in neighbors:
            n = "".join(n)
            if (n not in explored) and (n not in frontier_set.keys()):
                frontier.put((h(n) + depth + 1, n, depth + 1))
                frontier_set[n] = h(n) + depth + 1
                parent[n] = s
            elif (n not in explored) and (n in frontier_set):
                if frontier_set[n] > h(n) + depth + 1:
                    frontier.put((h(n) + depth + 1, n, depth + 1))
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
    print(f"\n## A* with {h.__name__} distance ##")
    print("\nsteps:\n")
    for i in list(steps):
        print(i)
    print("--------------------------------------------")
    print(f"expanded nodes: {len(explored)}")
    print(f"run time: {finish_time - start_time}s")
    print(f"cost of path: {len(steps) - 1}")
    print(f"search depth: {max_depth}")
    print("\n###############################################\n")


def manhattan(l):
    l = [[l[0], l[1], l[2]], [l[3], l[4], l[5]], [l[6], l[7], l[8]]]
    dist = 0
    for row in range(3):
        for col in range(3):
            if l[row][col] == '0':
                dist += abs(0 - row) + abs(0 - col)
            elif l[row][col] == '1':
                dist += abs(0 - row) + abs(1 - col)
            elif l[row][col] == '2':
                dist += abs(0 - row) + abs(2 - col)
            elif l[row][col] == '3':
                dist += abs(1 - row) + abs(0 - col)
            elif l[row][col] == '4':
                dist += abs(1 - row) + abs(1 - col)
            elif l[row][col] == '5':
                dist += abs(1 - row) + abs(2 - col)
            elif l[row][col] == '6':
                dist += abs(2 - row) + abs(0 - col)
            elif l[row][col] == '7':
                dist += abs(2 - row) + abs(1 - col)
            elif l[row][col] == '8':
                dist += abs(2 - row) + abs(2 - col)
    return dist


def euclidean(l):
    l = [[l[0], l[1], l[2]], [l[3], l[4], l[5]], [l[6], l[7], l[8]]]
    dist = 0
    for row in range(3):
        for col in range(3):
            if l[row][col] == '0':
                dist += math.sqrt((0 - row)**2 + (0 - col)**2)
            elif l[row][col] == '1':
                dist += math.sqrt((0 - row)**2 + (1 - col)**2)
            elif l[row][col] == '2':
                dist += math.sqrt((0 - row)**2 + (2 - col)**2)
            elif l[row][col] == '3':
                dist += math.sqrt((1 - row)**2 + (0 - col)**2)
            elif l[row][col] == '4':
                dist += math.sqrt((1 - row)**2 + (1 - col)**2)
            elif l[row][col] == '5':
                dist += math.sqrt((1 - row)**2 + (2 - col)**2)
            elif l[row][col] == '6':
                dist += math.sqrt((2 - row)**2 + (0 - col)**2)
            elif l[row][col] == '7':
                dist += math.sqrt((2 - row)**2 + (1 - col)**2)
            elif l[row][col] == '8':
                dist += math.sqrt((2 - row)**2 + (2 - col)**2)
    return dist


BFS(game)
DFS(game)
A_star(game, manhattan)
A_star(game, euclidean)
