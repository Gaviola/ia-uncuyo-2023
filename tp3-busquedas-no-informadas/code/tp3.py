import random
from colorama import init, Fore
from collections import deque
from queue import Queue


class GridEnvironment:
    def __init__(self, size=100, obstacle_percentage=20):
        self.size = size
        self.obstacle_percentage = obstacle_percentage
        self.grid = self.generate_random_grid()  # Genera una grilla aleatoria con obstáculos
        self.start = self.generate_random_position()  # Genera una posición de inicio aleatoria
        self.goal = self.generate_random_position()  # Genera una posición de destino aleatoria

        while (
            self.start == self.goal
            or self.grid[self.start[0]][self.start[1]]
            or self.grid[self.goal[0]][self.goal[1]]
        ):
            # Asegura que la posición inicial y el destino sean diferentes y no obstáculos
            self.start = self.generate_random_position()
            self.goal = self.generate_random_position()

    def generate_random_grid(self):
        grid = [[False for _ in range(self.size)] for _ in range(self.size)]
        num_obstacles = int((self.obstacle_percentage / 100) * (self.size * self.size))
        for _ in range(num_obstacles):
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            grid[x][y] = True
        return grid

    def generate_random_position(self):
        x = random.randint(0, self.size - 1)
        y = random.randint(0, self.size - 1)
        return x, y

    def is_valid_move(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size and not self.grid[x][y]

    def bfs(self):
        visited = [[False for _ in range(self.size)] for _ in range(self.size)]
        queue = Queue()
        queue.put((self.start, []))  # Inicialmente, no hay movimientos realizados
        visited[self.start[0]][self.start[1]] = True
        nodes_visited = 0  # Contador de nodos visitados

        while not queue.empty():
            current, moves = queue.get()
            nodes_visited += 1  # Incrementa el contador de nodos visitados

            if current == self.goal:
                return moves, nodes_visited  # Devuelve el camino y la cantidad de nodos visitados si llega al destino

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = current[0] + dx, current[1] + dy
                if self.is_valid_move(new_x, new_y) and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    new_moves = moves + [(new_x, new_y)]  # Agrega el nuevo movimiento
                    queue.put(((new_x, new_y), new_moves))

        return None, nodes_visited  # No se encontró un camino válido, pero se devuelve la cantidad de nodos visitados

    def dfs(self, max_depth=float('inf')):
        stack = deque([(self.start, [])])   # Usamos una pila y cada elemento es una tupla (posición, camino)
        shortest_path = None
        shortest_path_length = float('inf')
        nodes_visited = 0

        while stack:
            current, moves = stack.pop()
            nodes_visited += 1

            if current == self.goal:
                if len(moves) < shortest_path_length:
                    shortest_path_length = len(moves)
                    shortest_path = moves  # Actualiza el camino más corto

            if len(moves) < shortest_path_length and len(moves) < max_depth:
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_x, new_y = current[0] + dx, current[1] + dy
                    new_position = (new_x, new_y)
                    if self.is_valid_move(new_x, new_y) and new_position not in moves:
                        new_moves = moves + [new_position]  # Agrega el nuevo movimiento
                        stack.append((new_position, new_moves))

        return shortest_path, nodes_visited

    def print_grid(self, path):
        for y in range(self.size):
            for x in range(self.size):
                if (x, y) == self.start:
                    print(Fore.GREEN + "S", end=" ")
                elif (x, y) == self.goal:
                    print(Fore.CYAN + "D", end=" ")
                elif self.grid[x][y]:
                    print(Fore.RED + "#", end=" ")
                elif (x, y) in path:
                    print(Fore.BLUE + "*", end=" ")
                else:
                    print(Fore.WHITE + ".", end=" ")
            print()

    @staticmethod
    def execute(attempts):
        for i in range(attempts):
            size = 30
            obstacle_percentage = 8
            env = GridEnvironment(size, obstacle_percentage)

            path_bfs, nodes_visited_bfs = env.bfs()

            if path_bfs:
                env.print_grid(path_bfs)
                print(f"Cantidad de nodos visitados con BFS: {nodes_visited_bfs}")
            else:
                print("No se encontró un camino válido con BFS.")

            path_dfs, nodes_visited_dfs = env.dfs(size)

            if path_dfs:
                env.print_grid(path_dfs)
                print(f"Cantidad de nodos visitados con DFS: {nodes_visited_dfs}")
            else:
                print("No se encontró un camino válido con DFS.")


if __name__ == "__main__":
    GridEnvironment.execute(1)
