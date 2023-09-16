import csv
import heapq
import random
import statistics
from colorama import Fore
from queue import Queue

from matplotlib import pyplot as plt


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
        visited = [[False for _ in range(self.size)] for _ in range(self.size)]
        stack = [(self.start, [])]  # Utilizamos una pila en lugar de una cola para DFS
        nodes_visited = 0  # Contador de nodos visitados

        while stack:
            current, moves = stack.pop()
            nodes_visited += 1  # Incrementa el contador de nodos visitados

            if current == self.goal:
                return moves, nodes_visited  # Devuelve el camino y la cantidad de nodos visitados si llega al destino

            visited[current[0]][current[1]] = True

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = current[0] + dx, current[1] + dy
                if self.is_valid_move(new_x, new_y) and not visited[new_x][new_y] and len(moves) < max_depth:
                    new_moves = moves + [(new_x, new_y)]  # Agrega el nuevo movimiento
                    stack.append(((new_x, new_y), new_moves))

        return None, nodes_visited  # No se encontró un camino válido, pero se devuelve la cantidad de nodos visitados

    def uniform_cost_search(self):
        visited = [[False for _ in range(self.size)] for _ in range(self.size)]
        priority_queue = [(0, self.start, [])]  # Utilizamos una cola de prioridad (heap) para UCS
        nodes_visited = 0  # Contador de nodos visitados
    
        while priority_queue:
            cost, current, moves = heapq.heappop(priority_queue)
            nodes_visited += 1  # Incrementa el contador de nodos visitados
    
            if current == self.goal:
                return moves, nodes_visited  # Devuelve el camino y la cantidad de nodos visitados si llega al destino
    
            if not(visited[current[0]][current[1]]):

                visited[current[0]][current[1]] = True

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_x, new_y = current[0] + dx, current[1] + dy
                    if self.is_valid_move(new_x, new_y) and not visited[new_x][new_y]:
                        new_cost = cost + 1  # Costo uniforme
                        new_moves = moves + [(new_x, new_y)]  # Agrega el nuevo movimiento
                        heapq.heappush(priority_queue, (new_cost, (new_x, new_y), new_moves))
    
        return None, nodes_visited  # No se encontró un camino válido, pero se devuelve la cantidad de nodos visitados

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
    def print_plotbox(result: dict):

        fig, ax = plt.subplots()
        ax.boxplot(
            results.values(),
            labels=results.keys(),
            showmeans=True,
        )

        # Agregar título y etiquetas de ejes
        plt.title("Algoritmos de Búsqueda")
        plt.xlabel("Algoritmo de Búsqueda")
        plt.ylabel("Cantidad de Nodos Explorados")

        # Mostrar el gráfico
        plt.tight_layout()
        plt.show()

        print(f"Promedio de nodos visitados con BFS: {statistics.mean(result['BFS'])}")
        print(f"Desviación estándar de nodos visitados con BFS: {statistics.stdev(result['BFS'])}")

        print(f"Promedio de nodos visitados con DFS: {statistics.mean(result['DFS'])}")
        print(f"Desviación estándar de nodos visitados con DFS: {statistics.stdev(result['DFS'])}")

        print(f"Promedio de nodos visitados con DFS con profundidad limitada: {statistics.mean(result['DFS Limitado'])}")
        print(f"Desviación estándar de nodos visitados con DFS con profundidad limitada: {statistics.stdev(result['DFS Limitado'])}")

        print(f"Promedio de nodos visitados con UCS: {statistics.mean(result['UCS'])}")
        print(f"Desviación estándar de nodos visitados con UCS: {statistics.stdev(result['UCS'])}")

    @staticmethod
    def execute(attempts):

        bfs = ([], [])
        dfs = ([], [])
        dfs_limited = ([], [])
        ucs = ([], [])

        with open("C:\\Users\\Facu\\PycharmProjects\\ia-uncuyo-2023\\tp3-busquedas-no-informadas\\results.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Algorithm_name", "env_n", "estates_n", "solution_found"])
            for i in range(attempts):
                size = 100
                obstacle_percentage = 8
                env = GridEnvironment(size, obstacle_percentage)

                # Guardo los resultados de cada algoritmo en una lista para luego calcular el promedio y desviación estándar
                bfs_path, nodes_visited_bfs = env.bfs()
                bfs_solution = True
                if bfs_path is None:
                    bfs_path = []
                    bfs_solution = False
                bfs[0].append(bfs_path)
                bfs[1].append(nodes_visited_bfs)
                writer.writerow(["BFS", i, bfs[1][i], bfs_solution])

                dfs_path, nodes_visited_dfs = env.dfs()
                dfs_solution = True
                if dfs_path is None:
                    dfs_path = []
                    dfs_solution = False
                dfs[0].append(dfs_path)
                dfs[1].append(nodes_visited_dfs)
                writer.writerow(["DFS", i, dfs[1][i], dfs_solution])

                dfs_limited_path, nodes_visited_dfs_limited = env.dfs(1000)
                dfs_limited_solution = True
                if dfs_limited_path is None:
                    dfs_limited_path = []
                    dfs_limited_solution = False
                dfs_limited[0].append(dfs_limited_path)
                dfs_limited[1].append(nodes_visited_dfs_limited)
                writer.writerow(["DFS Limitado", i, dfs_limited[1][i], dfs_limited_solution])

                ucs_path, nodes_visited_ucs = env.uniform_cost_search()
                ucs_solution = True
                if ucs_path is None:
                    ucs_path = []
                    ucs_solution = False
                ucs[0].append(ucs_path)
                ucs[1].append(nodes_visited_ucs)
                writer.writerow(["UCS", i, ucs[1][i], ucs_solution])

        results = {
            "BFS": bfs[1],
            "DFS": dfs[1],
            "DFS Limitado": dfs_limited[1],
            "UCS": ucs[1],
        }
        return results


if __name__ == "__main__":
    results = GridEnvironment.execute(30)
    GridEnvironment.print_plotbox(results)
