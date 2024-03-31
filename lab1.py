import itertools

# Функція для обчислення значення логічного виразу
def evaluate(expression, interpretation):
    stack = []
    try:
        for char in expression:
            if char == 'x':
                stack.append(interpretation[0])
            elif char == 'y':
                stack.append(interpretation[1])
            elif char == 'z':
                stack.append(interpretation[2])
            elif char == '¬':
                stack.append(not stack.pop())
            elif char == '∨':
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand1 or operand2)
            elif char == '∧':
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand1 and operand2)
            elif char == '→':
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(not operand1 or operand2)
            elif char == '↔':
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append((not operand1 or operand2) and (not operand2 or operand1))
    except IndexError:
        return False  # Повертаємо False у випадку, якщо стек порожній
    return stack.pop()

# Функція для перевірки введених даних
def check_input(expression):
    valid_chars = {'x', 'y', 'z', '¬', '∨', '∧', '→', '↔', '(', ')'}
    for char in expression:
        if char not in valid_chars:
            return False
    return True

# Головна функція програми
def main():
    expression = input("Введіть вираз: ")
    
    if not check_input(expression):
        print("Некоректне введення даних!")
        return
    
    num_variables = int(input("Введіть кількість простих висловлювань: "))
    variables = ['x', 'y', 'z']
    interpretations = list(itertools.product([False, True], repeat=num_variables))

    print("\nТаблиця істинності:")
    print("-" * (num_variables * 5 + len(expression) + 4))
    print("|", end="")
    for var in variables[:num_variables]:
        print(f" {var} |", end="")
    print(f" {expression} |")
    print("-" * (num_variables * 5 + len(expression) + 4))
    
    for interpretation in interpretations:
        print("|", end="")
        for value in interpretation:
            print(f" {int(value)} |", end="")
        print(f"  {int(evaluate(expression, interpretation))}  |")
        print("-" * (num_variables * 5 + len(expression) + 4))

if __name__ == "__main__":
    main()
