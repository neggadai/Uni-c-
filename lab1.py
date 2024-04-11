"""
Написати на будь-якій відомій студентові мові програмування програму для 
реалізації програмного визначення значень таблиці істиності логічних 
висловлювань при різних інтерпретаціях
"""


import itertools

def infix_to_postfix(expression):
    value = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    postfix = []
    stack = []

    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  
        else:  
            while stack and value.get(stack[-1], 0) >= value.get(char, 0):
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)



infix_expression = "(a * b) + c"
postfix_expression = infix_to_postfix(infix_expression)
print("Постфиксное выражение:", postfix_expression)

# Функція для обчислення значення логічного виразу
def evaluate(expression, interpretation):
    stack = []
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

    return stack.pop()

# Функція для перевірки введених даних
def check_input(expression):
    valid_chars = {'x', 'y', 'z', '¬', '∨', '∧', '→', '↔', '(', ')', ' '}
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
