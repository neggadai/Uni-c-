"""
Створити з введених чисел матрицю відношення та визначити її тип
"""
def input_set(prompt):
    # Функція для введення множини чисел
    while True:
        try:
            elements = input(prompt).split()
            return [float(x) for x in elements]
        except ValueError:
            print("Будь ласка, введіть числа, розділені пробілами.")

def construct_relation_matrix(set_A, set_B):
    # Побудова матриці відношення
    matrix = []
    for a in set_A:
        row = []
        for b in set_B:
            row.append(int(a < b))
        matrix.append(row)
    return matrix

def print_relation_matrix(matrix):
    # Виведення матриці відношення
    for row in matrix:
        print(row)

def check_relation_type(matrix):
    # Перевірка типу відношення
    reflexive = all(matrix[i][i] == 1 for i in range(len(matrix)))
    symmetric = all(matrix[i][j] == matrix[j][i] for i in range(len(matrix)) for j in range(len(matrix)))
    antisymmetric = all(matrix[i][j] != matrix[j][i] for i in range(len(matrix)) for j in range(len(matrix)) if i != j)
    transitive = all(matrix[i][j] == 1 for i in range(len(matrix)) for j in range(len(matrix)) for k in range(len(matrix)) if matrix[i][k] == 1 and matrix[k][j] == 1)
    
    print("Тип відношення:")
    print("Рефлексивне: ", "Так" if reflexive else "Ні")
    print("Симетричне: ", "Так" if symmetric else "Ні")
    print("Антисиметричне: ", "Так" if antisymmetric else "Ні")
    print("Транзитивне: ", "Так" if transitive else "Ні")

def main():
    set_A = input_set("Введіть елементи множини A, розділені пробілами: ")
    set_B = input_set("Введіть елементи множини B, розділені пробілами: ")

    relation_matrix = construct_relation_matrix(set_A, set_B)

    print("\nМатриця відношення:")
    print_relation_matrix(relation_matrix)

    check_relation_type(relation_matrix)

if __name__ == "__main__":
    main()
