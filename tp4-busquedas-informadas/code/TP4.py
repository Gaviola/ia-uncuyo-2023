import heapq
import random
import statistics

import pygame
from queue import PriorityQueue
from collections import deque

from colorama import Fore
from matplotlib import pyplot as plt

WIDTH = 900
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Matrix")
OBSTACLE_RATE = 8
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Environment:
    def __init__(self, size):
        self.size = size
        self.start = None
        self.goal = None
        self.grid = self.make_grid()

    def make_grid(self):
        grid = []

        start_slot = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
        end_slot = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
        if start_slot == end_slot:
            while start_slot == end_slot:
                start_slot = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
                end_slot = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))

        gap = WIDTH // self.size
        for i in range(self.size):
            grid.append([])
            for j in range(self.size):
                if (i,j) == start_slot:
                    self.start = Slot(i, j, gap, self.size)
                    self.start.make_start()
                    grid[i].append(self.start)

                elif (i,j) == end_slot:
                    self.goal = Slot(i, j, gap, self.size)
                    self.goal.make_end()
                    grid[i].append(self.goal)
                else:
                    slot = Slot(i, j, gap, self.size)
                    grid[i].append(slot)
                    # Asigna el inicio y el final de manera aleatoria
                    if random.randint(0, 100) < OBSTACLE_RATE:
                        slot.make_barrier()
    
        return grid

    def draw_grid(self, win):
        gap = WIDTH // self.size
        for i in range(self.size):
            pygame.draw.line(win, GREY, (0, i * gap), (WIDTH, i * gap))
            pygame.draw.line(win, GREY, (i * gap, 0), (i * gap, WIDTH))

    def draw(self, win):
        win.fill(WHITE)
        for row in self.grid:
            for slot in row:
                slot.draw(win)
    
        self.draw_grid(win)
        pygame.display.update()

    def clean_grid(self):
        for row in self.grid:
            for slot in row:
                if slot.is_open() or slot.is_closed() or slot.is_path():
                    slot.reset()

    def draw_path(self, win, path):
        win.fill(WHITE)
    
        for row in self.grid:
            for slot in row:
                slot.draw(win)
    
        self.draw_grid(win)
        for slot in path:
            slot.make_path()
            slot.draw(win)
        pygame.display.update()

    def print_grid(self, path):
        for y in range(self.size):
            for x in range(self.size):
                sol = False
                if (x, y) == self.start.get_pos():
                    print(Fore.GREEN + "S", end=" ")
                elif (x, y) == self.goal.get_pos():
                    print(Fore.CYAN + "D", end=" ")
                elif self.grid[x][y].is_barrier():
                    print(Fore.RED + "#", end=" ")
                else:
                    for slot in path:
                        if (x, y) == slot.get_pos():
                            print(Fore.BLUE + "*", end=" ")
                            sol = True
                    if not sol:
                        print(Fore.WHITE + ".", end=" ")

            print()



class Slot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_path(self):
        return self.color == PURPLE

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2-x1) + abs(y2-y1)


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
        current.make_path()

    return path


def a_estrella(env: Environment, print_grid=False):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, env.start))
    came_from = {}
    g_score = {spot: float("inf") for row in env.grid for spot in row}
    g_score[env.start] = 0
    f_score = {spot: float("inf") for row in env.grid for spot in row}
    f_score[env.start] = h(env.start.get_pos(), env.goal.get_pos())
    
    open_set_hash = {env.start}
    
    while not open_set.empty():
    
        current = open_set.get()[2]
        open_set_hash.remove(current)
        current.update_neighbors(env.grid)
    
        if current == env.goal:
            reconstruct_path(came_from, env.goal)
            env.goal.make_end()
            env.start.make_start()

            if print_grid:
                running = True
                while running:
                    env.draw(WIN)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False

            return count
    
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
    
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), env.goal.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
    
        if current != env.start:
            current.make_closed()
    
    return None


def bfs(env: Environment, print_grid=False):
    count = 0
    queue = deque()
    queue.append(env.start)
    came_from = {}
    visited = set()
    
    while queue:
        current = queue.popleft()
        visited.add(current)
        current.update_neighbors(env.grid)
    
        if current == env.goal:
            reconstruct_path(came_from, env.goal)
            env.goal.make_end()
            env.start.make_start()

            if print_grid:
                running = True
                while running:
                    env.draw(WIN)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False

            return count
    
        for neighbor in current.neighbors:
            if neighbor not in visited:
                count += 1
                queue.append(neighbor)
                came_from[neighbor] = current
                visited.add(neighbor)
                neighbor.make_open()
    
        if current != env.start:
            current.make_closed()
    
    return None


def dfs(env: Environment, limit=0, print_grid=False):
    count = 0
    stack = [(env.start, 0)]
    visited = set()
    came_from = {}
    if limit == 0:
        limit = env.size * env.size

    while stack:
        current, depth = stack.pop()
        visited.add(current)
        current.update_neighbors(env.grid)

        if current == env.goal:
            reconstruct_path(came_from, env.goal)
            env.goal.make_end()
            env.start.make_start()

            if print_grid:
                running = True
                while running:
                    env.draw(WIN)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False

            return count

        if depth < limit:
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    count += 1
                    stack.append((neighbor, depth + 1))
                    came_from[neighbor] = current
                    neighbor.make_open()

        if current != env.start:
            current.make_closed()

    return None


def ucs(env: Environment, print_grid=False):
    count = 0
    heap = [(0, count, env.start)]
    came_from = {}
    cost_so_far = {spot: float("inf") for row in env.grid for spot in row}
    cost_so_far[env.start] = 0

    while heap:
        _, _, current = heapq.heappop(heap)

        if current == env.goal:
            reconstruct_path(came_from, env.goal)
            env.goal.make_end()
            env.start.make_start()

            if print_grid:
                running = True
                while running:
                    env.draw(WIN)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False

            return count

        current.update_neighbors(env.grid)

        for neighbor in current.neighbors:
            new_cost = cost_so_far[current] + 1  # Costo uniforme

            if new_cost < cost_so_far[neighbor]:
                count += 1
                cost_so_far[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, count, neighbor))
                came_from[neighbor] = current
                neighbor.make_open()

        if current != env.start:
            current.make_closed()

    return None


def print_boxplot(result):

    fig, ax = plt.subplots()
    ax.boxplot(
        result.values(),
        labels=result.keys(),
        showmeans=True,
    )

    # Agregar título y etiquetas de ejes
    plt.title("Algoritmos de Búsqueda Informada")
    plt.xlabel("Algoritmo de Búsqueda")
    plt.ylabel("Cantidad de Nodos Explorados")

    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()

    print(f"Promedio de nodos visitados con BFS: {statistics.mean(result['bfs'])}")
    print(
        f"Desviación estándar de nodos visitados con BFS: {statistics.stdev(result['bfs'])}"
    )

    print(f"Promedio de nodos visitados con DFS: {statistics.mean(result['dfs'])}")
    print(
        f"Desviación estándar de nodos visitados con DFS: {statistics.stdev(result['dfs'])}"
    )

    print(
        f"Promedio de nodos visitados con DFS con profundidad limitada: {statistics.mean(result['dfs_limited'])}"
    )
    print(
        f"Desviación estándar de nodos visitados con DFS con profundidad limitada: {statistics.stdev(result['dfs_limited'])}"
    )

    print(f"Promedio de nodos visitados con UCS: {statistics.mean(result['ucs'])}")
    print(
        f"Desviación estándar de nodos visitados con UCS: {statistics.stdev(result['ucs'])}"
    )
    print(f"Promedio de nodos visitados con A*: {statistics.mean(result['a_estrella'])}")
    print(
        f"Desviación estándar de nodos visitados con A*: {statistics.stdev(result['a_estrella'])}"
    )


def execute(attempts):
    size = 100
    print_grid = False
    results = {
        'bfs': [],
        'dfs': [],
        'dfs_limited': [],
        'ucs': [],
        'a_estrella': []
    }

    for i in range(attempts):
        env = Environment(size)

        nodes_visited = bfs(env, print_grid)
        if nodes_visited is None:
            nodes_visited = 0
        results["bfs"].append(nodes_visited)
        env.clean_grid()

        nodes_visited = dfs(env, print_grid)
        if nodes_visited is None:
            nodes_visited = 0
        results["dfs"].append(nodes_visited)
        env.clean_grid()

        nodes_visited = dfs(env, 1000, print_grid)
        if nodes_visited is None:
            nodes_visited = 0
        results["dfs_limited"].append(nodes_visited)
        env.clean_grid()

        nodes_visited = ucs(env, print_grid)
        if nodes_visited is None:
            nodes_visited = 0
        results["ucs"].append(nodes_visited)
        env.clean_grid()

        nodes_visited = a_estrella(env, print_grid)
        if nodes_visited is None:
            nodes_visited = 0
        results["a_estrella"].append(nodes_visited)
        env.clean_grid()

    return results


if __name__ == "__main__":
    attempts = 30
    result = execute(attempts)
    print_boxplot(result)