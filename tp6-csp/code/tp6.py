import time
import csv
from matplotlib import pyplot as plt


class Board:
    def __init__(self, size):
        self.size = size
        self.num_queens = size
        self.queens = []

    def draw_board(self, punctuations=True):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) in self.queens:
                    print("Q", end=" ")
                else:
                    print("-", end=" ")
            print()

    def __copy__(self):
        board = Board(self.size)
        board.queens = self.queens.copy()
        return board

    def __del__(self):
        del self.queens


def exist_conflict(current_queen, queens):
    for queen in queens:
        if queen[0] == current_queen[0]:
            return True
        elif queen[1] == current_queen[1]:
            return True
        elif queen[0] - current_queen[0] == queen[1] - current_queen[1]:
            return True
        elif queen[0] + queen[1] == current_queen[0] + current_queen[1]:
            return True
    return False


# Funcion que busca una solucion al problema de las n reinas, utilizando un enfoque de CSP con backtracking
def backtracking(board, current_sol, states=0):
    if board.size == len(current_sol):
        return current_sol, states

    for i in range(board.size):
        j = len(current_sol)
        states += 1
        if not exist_conflict((i, j), current_sol):
            current_sol.append((i, j))
            solution, states = backtracking(board, current_sol, states)
            if solution:
                return solution, states
            current_sol.pop()
    return None, states


def forward_checking(board, current_sol, states=0):
    if board.size == len(current_sol):
        return current_sol, states

    # Seleccionar la próxima variable (columna) a asignar utilizando una heurística
    next_column = select_variable(board, current_sol)

    for i in range(board.size):
        j = len(current_sol)
        states += 1
        if not exist_conflict((i, next_column), current_sol):
            # Realizar la asignación
            current_sol.append((i, next_column))

            # Actualizar los dominios de las variables (reinas)
            update_domains(board, current_sol, next_column)

            solution, states = forward_checking(board, current_sol, states)
            if solution:
                return solution, states

            # Deshacer la asignación y restaurar los dominios
            current_sol.pop()
            restore_domains(board, current_sol, next_column)

    return None, states


def select_variable(board, current_sol):
    # Obtener todas las columnas que aún no tienen una reina asignada
    unassigned_columns = [col for col in range(board.size) if col not in [queen[1] for queen in current_sol]]

    # Usar la heurística MRV para seleccionar la columna con el dominio más pequeño
    min_remaining_values = float('inf')
    selected_column = None

    for column in unassigned_columns:
        remaining_values = count_remaining_values(board, current_sol, column)
        if remaining_values < min_remaining_values:
            min_remaining_values = remaining_values
            selected_column = column

    return selected_column


def count_remaining_values(board, current_sol, column):
    # Contar la cantidad de valores posibles que quedan en el dominio de una columna
    remaining_values = 0
    for i in range(board.size):
        if not exist_conflict((i, column), current_sol):
            remaining_values += 1
    return remaining_values


def update_domains(board, current_sol, column):
    # Actualizar los dominios de las variables (reinas) después de realizar una asignación.
    # Se eliminan las posiciones en la misma fila y diagonales como dominios posibles.
    to_remove = []
    for queen in board.queens:
        if queen[1] == column or exist_conflict(queen, current_sol):
            to_remove.append(queen)  # Marcar para eliminar

    for queen in to_remove:
        board.queens.remove(queen)  # Eliminar las reinas marcadas


def restore_domains(board, current_sol, column):
    # Restaurar los dominios de las variables (reinas) después de deshacer una asignación.
    # En este ejemplo, se restauran las posiciones eliminadas durante la asignación.
    for queen in current_sol:
        if queen not in board.queens:
            board.queens.append(queen)


def execute(attempts):
    # EJ: backtraking: [[estados], [tiempo]]
    result = {
        "backtracking": [[], []],
        "forward_checking": [[], []]
    }
    sizes = [4, 8, 10, 12, 15]

    with open(
        "C:\\Users\\Facu\\PycharmProjects\\ia-uncuyo-2023\\tp6-csp\\results.csv",
        "w",
        newline="",
    ) as file:
        writer = csv.writer(file)
        writer.writerow(
            [f"Algorithm_name", "Size", "States", "Time (Seconds)"]
        )
        for (_, size) in enumerate(sizes):
            for i in range(attempts):
                board = Board(size)
                start_time = time.time()
                solution, states = backtracking(board, [])
                end_time = time.time()
                result["backtracking"][0].append(states)
                result["backtracking"][1].append(end_time - start_time)

                writer.writerow(
                    [
                        "Backtracking",
                        size,
                        states,
                        end_time - start_time,
                        ]
                )

                start_time = time.time()
                solution, states = forward_checking(board, [])
                end_time = time.time()
                result["forward_checking"][0].append(states)
                result["forward_checking"][1].append(end_time - start_time)

                writer.writerow(
                    [
                        "Forward Checking",
                        size,
                        states,
                        end_time - start_time,
                        ]
                )

            result_times = {
                "backtracking": result["backtracking"][1],
                "forward_checking": result["forward_checking"][1],
            }

            result_states = {
                "backtracking": result["backtracking"][0],
                "forward_checking": result["forward_checking"][0],
            }

            print_plotbox(
                result_times,
                f"CSP N-Reinas Tiempos (size = {size})",
                "Algoritmo de CSP",
                "Tiempo (segundos)",
            )

            print_plotbox(
                result_states,
                f"CSP N-Reinas Estados (size = {size})",
                "Algoritmo de CSP",
                "Estados",
            )
    return result


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
    execute(5)
