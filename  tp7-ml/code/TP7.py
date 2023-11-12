import pandas as pd
import numpy as np


# Función para calcular B(q)
def B(q):
    if q == 0 or q == 1:
        return 0  # Evitar divisiones por cero y logaritmos de cero
    return -(q * np.log2(q) + (1 - q) * np.log2(1 - q))


# Función para calcular el Remainder (A)
def remainder(A, examples):
    values = np.unique(examples[A])
    p, n = len(examples[examples["play"] == "yes"]), len(
        examples[examples["play"] == "no"]
    )
    remainder = 0

    for value in values:
        exs = examples[examples[A] == value]
        pk, nk = len(exs[exs["play"] == "yes"]), len(exs[exs["play"] == "no"])
        remainder += ((pk + nk) / (p + n)) * B(pk / (pk + nk))

    return remainder


# Función para calcular la entropía
def calcular_entropia(examples: pd.DataFrame, attribute):
    p, n = len(examples[examples["play"] == "yes"]), len(
        examples[examples["play"] == "no"]
    )
    b_pn = B(p / (p + n))
    rem = remainder(
        attribute, examples
    )
    gain = b_pn - rem
    return gain


# Define la función IMPORTANCE (puedes ajustarla según tus necesidades)
def importance(attribute, examples):
    # Calcula la entropía antes de dividir en función del atributo
    entropy_before = calcular_entropia(examples, attribute)

    # Inicializa la suma de entropías ponderadas después de dividir
    weighted_entropy_after = 0.0

    # Itera sobre los posibles valores del atributo
    for value in np.unique(examples[attribute]):
        exs = examples[examples[attribute] == value]
        weighted_entropy_after += (len(exs) / len(examples)) * calcular_entropia(
            exs, attribute
        )

    # Calcula la ganancia de información
    information_gain = entropy_before - weighted_entropy_after

    return information_gain


# Define la función PLURALITY-VALUE
def plurality_value(examples):
    # Cuenta las etiquetas de clasificación
    counts = (examples["play"]).value_counts()

    # Encuentra la etiqueta más común
    most_common = counts.most_common()

    # Maneja empates eligiendo aleatoriamente entre las etiquetas más comunes
    tiebreak = [item for item in most_common if item[1] == most_common[0][1]]
    if len(tiebreak) > 1:
        return np.random.choice(tiebreak)[0]
    else:
        return most_common[0][0]
    pass


# Define la función DECISION-TREE-LEARNING
def decision_tree(
    examples: pd.DataFrame, attributes, parent_examples, used_attributes=[]
):
    if len(examples) == 0:
        return plurality_value(parent_examples)
    elif (examples["play"] == examples["play"].iloc[0]).all():
        return examples["play"].iloc[0]
    elif len(attributes) == 0:
        return plurality_value(examples)
    else:
        available_attributes = [attr for attr in attributes if attr != "play"]
        A = max(available_attributes, key=lambda a: importance(a, examples))
        used_attributes.append(A)
        tree = {"attribute": A, "branches": {}}
        for vk in np.unique(examples[A]):
            exs = examples[examples[A] == vk]
            subtree = decision_tree(
                exs,
                [attr for attr in attributes if attr != A],
                examples,
                used_attributes,
            )
            tree["branches"][vk] = subtree
        used_attributes.remove(A)
        return tree


def print_decision_tree(tree, indent=""):
    if "attribute" in tree:
        print(indent + str(tree["attribute"]) + ":")
        for branch, subtree in tree["branches"].items():
            print(indent + "|-- " + str(branch))
            print_decision_tree(subtree, indent + "    ")
    else:
        print(indent + str(tree))


if __name__ == "__main__":
    data = pd.read_csv(
        "C:\\Users\\Facu\\PycharmProjects\\ia-uncuyo-2023\\ tp7-ml\\data\\tennis.csv"
    )
    attributes = data.columns.tolist()
    result = decision_tree(data, attributes, None)
    print_decision_tree(result)
