import csv
import random
import math
import statistics
import time

from matplotlib import pyplot as plt


class Board:
    def __init__(self, size):
        self.size = size
        self.num_queens = size
        self.queens = []
        self.cost = 0

    def generate_queens(self, fixed_column=False):
        # Genera reinas aleatoriamente por columna
        if not fixed_column:
            for i in range(self.size):
                queen = (i, random.randint(0, self.size - 1))
                self.queens.append(queen)
        # Genera reinas aleatoriamente en cualquier posicion
        else:
            for i in range(self.size):
                queen = (
                    random.randint(0, self.size - 1),
                    random.randint(0, self.size - 1),
                )
                self.queens.append(queen)

    def draw_board(self, punctuations=True):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) in self.queens:
                    print("Q", end=" ")
                else:
                    print("-", end=" ")
            print()
        if punctuations:
            print(f"Costo: {self.cost}")

    def __copy__(self):
        board = Board(self.size)
        board.queens = self.queens.copy()
        return board

    def calculate_conflicts(self):
        conflicts = 0
        for i in range(self.size):
            queen1 = self.queens[i]
            for j in range(i + 1, self.size):
                queen2 = self.queens[j]
                # Horizontales y verticales
                if queen1[0] == queen2[0]:
                    conflicts += 1
                elif queen1[1] == queen2[1]:
                    conflicts += 1
                # Diagonales
                elif queen1[0] - queen2[0] == queen1[1] - queen2[1]:
                    conflicts += 1
                elif queen1[0] + queen1[1] == queen2[0] + queen2[1]:
                    conflicts += 1

        self.cost = conflicts
        return conflicts


def find_best_neighbors(board, max_states=1000):
    best_neighbor = None
    best_neighbor_cost = float("inf")
    states_founds = 0
    for i in range(board.size):
        for j in range(board.size):
            if (i, j) not in board.queens and states_founds < max_states:
                states_founds += 1
                new_board = board.__copy__()
                new_board.queens = [(i, j)] + [
                    (x, y) for x, y in board.queens if x != i
                ]  # Mueva una reina a la nueva posición
                new_board.calculate_conflicts()
                if new_board.cost < best_neighbor_cost:
                    best_neighbor = new_board
                    best_neighbor_cost = new_board.cost

    return best_neighbor, best_neighbor_cost, states_founds


def hill_climbing(board, max_states=3000):
    local_max_found = False
    best_solution = board
    best_solution_cost = board.calculate_conflicts()
    states_used = 0
    while not local_max_found:
        # Generar vecinos y encontrar el mejor vecino
        best_neighbor, best_neighbor_cost, states_number = find_best_neighbors(
            best_solution
        )
        states_used += states_number

        # Si el costo del mejor vecino es igual o mayor que el costo actual, detenerse
        if (
            best_neighbor_cost >= best_solution_cost or states_used >= max_states
        ) or best_neighbor_cost == 0:
            local_max_found = True

        # Si el costo del mejor vecino es menor, actualizar el tablero actual
        best_solution = best_neighbor
        best_solution_cost = best_neighbor_cost

    print(f"Estados Recorridos: {states_used}")
    best_solution.draw_board()
    return best_solution, best_solution_cost, states_used


def acceptance_probability(delta_cost, current_value):
    if delta_cost < 0:
        return 1.0
    else:
        return math.exp(-delta_cost / current_value)


def anneling(board, max_states=3000, initial_value=1000, decrease_rate=0.9):
    current_solution = board
    current_cost = current_solution.calculate_conflicts()
    current_value = initial_value
    final_states = 0

    for states_visited in range(max_states + 1):
        if current_cost == 0:
            print(f"Estados Recorridos: {states_visited}")
            current_solution.draw_board()
            return (
                current_solution,
                current_cost,
                final_states,
            )  # Encontramos una solución válida

        neighbor = current_solution.__copy__()  # Generar un vecino aleatorio
        row_to_move = random.randint(0, neighbor.size - 1)

        # Mover la reina solo en su propia columna
        current_column = neighbor.queens[row_to_move][1]
        new_column = random.randint(0, neighbor.size - 1)
        while new_column == current_column:
            new_column = random.randint(0, neighbor.size - 1)

        neighbor.queens[row_to_move] = (row_to_move, new_column)
        neighbor_cost = neighbor.calculate_conflicts()

        delta_cost = neighbor_cost - current_cost

        if delta_cost < 0 or random.random() < acceptance_probability(
            delta_cost, current_value
        ):
            current_solution = neighbor
            current_cost = neighbor_cost

        current_value *= decrease_rate
        final_states = states_visited

    print(f"Estados Recorridos: {final_states}")
    current_solution.draw_board()
    return current_solution, current_cost, final_states


# Divide la lista de reinas de los padres en 2 partes de igual longitud (siempre que sea posible) y crea el 1er hijo con la
# primera mitad de un padre y la segunda mitad del otro. De manera analoga, crea el 2do hijo con las mitades restantes
def crossover(parent1, parent2, board_size):
    crossover_point = random.randint(1, board_size // 2)
    child1 = Board(board_size)
    child2 = Board(board_size)
    child1.queens = parent1.queens[:crossover_point] + parent2.queens[crossover_point:]
    child2.queens = parent2.queens[:crossover_point] + parent1.queens[crossover_point:]
    child1.calculate_conflicts()
    child2.calculate_conflicts()
    return child1, child2


# El individuo se moverá a una nueva columna en la misma fila con una probabilidad de
# mutation_rate (0.50 por defecto). y con una probabilidad de 1 - mutation_rate, se moverá a una
# nueva fila con la misma columna. (Pueden ocurrir ambas)
def mutate(individual, board_size, mutation_rate=0.5):
    # Aplica mutación a un individuo
    if random.random() < mutation_rate:
        index_to_mutate = random.randint(0, board_size - 1)
        new_column = random.randint(0, board_size - 1)
        individual.queens[index_to_mutate] = (
            new_column,
            individual.queens[index_to_mutate][1],
        )
    if random.random() < 1 - mutation_rate:
        index_to_mutate = random.randint(0, board_size - 1)
        new_row = random.randint(0, board_size - 1)
        individual.queens[index_to_mutate] = (
            individual.queens[index_to_mutate][0],
            new_row,
        )


# En cada iteración, se seleccionarán 15 individuos al azar de la población, y los 2 mejores individuos con
# la mejor aptitud (menos conflictos) se eligen como los padres.
def select_parents(population):
    candidates = random.sample(population, 15)
    candidates.sort(key=lambda x: x.cost)
    parent1 = candidates[0]
    parent2 = candidates[1]
    return parent1, parent2


def genetic_algorithm(
    board_size, population_size=50, max_generations=3000, mutation_rate=0.5
):
    population = [Board(board_size) for _ in range(population_size)]
    generations = 0
    for board in population:
        board.generate_queens()

    for generation in range(max_generations):
        # Calcular la aptitud de la población actual
        fitness_scores = [board.calculate_conflicts() for board in population]

        # Selección y cruce para generar una nueva población
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2, board_size)
            mutate(child1, board_size)
            mutate(child2, board_size)
            new_population.extend([child1, child2])

        # Dejo los mejores individuos de la población anterior y la nueva población (la mejor mitad de cada uno)
        population.sort(key=lambda x: x.cost)
        new_population.sort(key=lambda x: x.cost)
        population = (
            population[: population_size // 2] + new_population[: population_size // 2]
        )

        fitness_scores = [board.cost for board in population]

        generations += 1
        # Comprobar si se ha encontrado una solución
        if 0 in fitness_scores:
            print(f"Estados Recorridos: {generations}")
            best_individual = population[fitness_scores.index(0)]
            best_individual.draw_board()
            return best_individual, min(fitness_scores), generations

    # Si no se encuentra una solución en max_generations, devolver el mejor individuo
    best_individual = population[fitness_scores.index(min(fitness_scores))]
    print(f"Estados Recorridos: {generations}")
    best_individual.draw_board()
    return best_individual, min(fitness_scores), generations


def execute(attempts):
    # EJ: "Hill Climbing" =  [[Solucion], [Costo], [Estados recorridos], [Tiempo]]
    result = {
        "Hill Climbing": [[], [], [], []],
        "Simulated Annealing": [[], [], [], []],
        "Genetic Algorithm": [[], [], [], []],
    }
    sizes = [4, 8, 10, 12, 15]
    all_size_result = []
    with open(
        "C:\\Users\\Facu\\PycharmProjects\\ia-uncuyo-2023\\tp5-busquedas-locales\\results.csv",
        "w",
        newline="",
    ) as file:
        writer = csv.writer(file)
        for size in enumerate(sizes):
            writer.writerow(
                [f"Algorithm_name (size)", "Cost", "States", "Solution_found", "Time (Seconds)"]
            )
            for i in range(attempts):
                board_hill = Board(size[1])
                board_hill.generate_queens()
                board_annealing = board_hill.__copy__()

                # Hill Climbing
                solution_found = False
                start_time = time.time()
                solution_hill, cost_hill, states_hill = hill_climbing(board_hill)
                end_time = time.time()
                result["Hill Climbing"][0].append(solution_hill)
                result["Hill Climbing"][1].append(cost_hill)
                result["Hill Climbing"][2].append(states_hill)
                result["Hill Climbing"][3].append(end_time - start_time)
                if cost_hill == 0:
                    solution_found = True
                writer.writerow(
                    [
                        f"Hill Climbing ({size[1]})",
                        cost_hill,
                        states_hill,
                        solution_found,
                        end_time - start_time,
                        ]
                )

                # Simulated Annealing
                solution_found = False
                start_time = time.time()
                solution_annealing, cost_annealing, states_anneling = anneling(
                    board_annealing
                )
                end_time = time.time()
                result["Simulated Annealing"][0].append(solution_annealing)
                result["Simulated Annealing"][1].append(cost_annealing)
                result["Simulated Annealing"][2].append(states_anneling)
                result["Simulated Annealing"][3].append(end_time - start_time)
                if cost_annealing == 0:
                    solution_found = True
                writer.writerow(
                    [
                        f"Simulated Annealing ({size[1]})",
                        cost_annealing,
                        states_anneling,
                        solution_found,
                        end_time - start_time,
                        ]
                )

                # Genetic Algorithm
                solution_found = False
                start_time = time.time()
                solution_genetic, cost_genetic, states_genetic = genetic_algorithm(
                    size[1]
                )
                end_time = time.time()
                result["Genetic Algorithm"][0].append(solution_genetic)
                result["Genetic Algorithm"][1].append(cost_genetic)
                result["Genetic Algorithm"][2].append(states_genetic)
                result["Genetic Algorithm"][3].append(end_time - start_time)
                if cost_genetic == 0:
                    solution_found = True
                writer.writerow(
                    [
                        f"Genetic Algorithm ({size[1]})",
                        cost_genetic,
                        states_genetic,
                        solution_found,
                        end_time - start_time,
                        ]
                )
            all_size_result.append(result.copy())

            result_times = {
                "Hill Climbing": result["Hill Climbing"][3],
                "Simulated Annealing": result["Simulated Annealing"][3],
                "Genetic Algorithm": result["Genetic Algorithm"][3]
            }

            result_costs = {
                "Hill Climbing": result["Hill Climbing"][1],
                "Simulated Annealing": result["Simulated Annealing"][1],
                "Genetic Algorithm": result["Genetic Algorithm"][1]
            }

            print_plotbox(
                result_times,
                f"Algoritmos de Búsqueda Local (size = {size[1]})",
                "Algoritmo de Búsqueda Local",
                "Tiempo de Ejecución (segundos)",
            )

            print_plotbox(
                result_costs,
                f"Algoritmos de Búsqueda Local (size = {size[1]})",
                "Algoritmo de Búsqueda Local",
                "Costo (conflictos entre reinas)"
            )

            writer.writerow([])
            writer.writerow(
                [
                    f"Algorithm_name (size)",
                    "States_mean",
                    "States_deviation",
                    "Solution_found_rate (%)",
                    "Time_mean (Seconds)",
                    "Time_deviation (Seconds)",
                ]
            )
            #for size in enumerate(sizes):
            writer.writerow(
                [
                    f"Hill Climbing ({size[1]})",
                    statistics.mean(result["Hill Climbing"][2]),
                    statistics.stdev(result["Hill Climbing"][2]),
                    result["Hill Climbing"][1].count(0) / attempts,
                    statistics.mean(result["Hill Climbing"][3]),
                    statistics.stdev(result["Hill Climbing"][3]),
                    ]
            )

            writer.writerow(
                [
                    f"Simulated Annealing ({size[1]})",
                    statistics.mean(result["Simulated Annealing"][2]),
                    statistics.stdev(result["Simulated Annealing"][2]),
                    result["Simulated Annealing"][1].count(0) / attempts,
                    statistics.mean(result["Simulated Annealing"][3]),
                    statistics.stdev(result["Simulated Annealing"][3]),
                    ]
            )

            writer.writerow(
                [
                    f"Genetic Algorithm ({size[1]})",
                    statistics.mean(result["Genetic Algorithm"][2]),
                    statistics.stdev(result["Genetic Algorithm"][2]),
                    result["Genetic Algorithm"][1].count(0) / attempts,
                    statistics.mean(result["Genetic Algorithm"][3]),
                    statistics.stdev(result["Genetic Algorithm"][3]),
                    ]
            )
            writer.writerow([])

            for key in result.keys():
                result[key] = [[], [], [], []]

    return all_size_result


def print_plotbox(result: dict, title, xlabel, ylabel):
    fig, ax = plt.subplots()
    ax.boxplot(
        result.values(),
        labels=result.keys(),
        showmeans=True,
    )

    # Agregar título y etiquetas de ejes
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()




if __name__ == "__main__":
    result = execute(30)



