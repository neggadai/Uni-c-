#include <iostream>
#include <vector>
#include <string>
#include <bitset>

using namespace std;

// Функція для обчислення значення логічного виразу
bool evaluate(string expression, vector<bool> interpretation) {
    vector<bool> stack;
    try {
        for (char& c : expression) {
            if (c == 'x') {
                stack.push_back(interpretation[0]);
            } else if (c == 'y') {
                stack.push_back(interpretation[1]);
            } else if (c == 'z') {
                stack.push_back(interpretation[2]);
            } else if (c == '¬') {
                bool operand = stack.back();
                stack.pop_back();
                stack.push_back(!operand);
            } else if (c == '∨') {
                bool operand2 = stack.back();
                stack.pop_back();
                bool operand1 = stack.back();
                stack.pop_back();
                stack.push_back(operand1  operand2);
            } else if (c == '∧') {
                bool operand2 = stack.back();
                stack.pop_back();
                bool operand1 = stack.back();
                stack.pop_back();
                stack.push_back(operand1 && operand2);
            } else if (c == '→') {
                bool operand2 = stack.back();
                stack.pop_back();
                bool operand1 = stack.back();
                stack.pop_back();
                stack.push_back(!operand1  operand2);
            } else if (c == '↔️') {
                bool operand2 = stack.back();
                stack.pop_back();
                bool operand1 = stack.back();
                stack.pop_back();
                stack.push_back((!operand1  operand2) && (!operand2  operand1));
            }
        }
    } catch (const std::out_of_range& e) {
        return false; // Повертаємо false у випадку, якщо стек порожній
    }
    return stack.back();
}

// Функція для перевірки введених даних
bool check_input(string expression) {
    set<char> valid_chars = {'x', 'y', 'z', '¬', '∨', '∧', '→', '↔️', '(', ')'};
    for (char& c : expression) {
        if (valid_chars.find(c) == valid_chars.end()) {
            return false;
        }
    }
    return true;
}

// Головна функція програми
int main() {
    string expression;
    cout << "Введіть вираз: ";
    getline(cin, expression);
    
    if (!check_input(expression)) {
        cout << "Некоректне введення даних!" << endl;
        return 1;
    }
    
    int num_variables;
    cout << "Введіть кількість простих висловлювань: ";
    cin >> num_variables;

    vector<char> variables = {'x', 'y', 'z'};
    vector<vector<bool>> interpretations;
    for (int i = 0; i < (1 << num_variables); ++i) {
        vector<bool> interpretation;
        for (int j = 0; j < num_variables; ++j) {
            interpretation.push_back((i >> j) & 1);
        }
        interpretations.push_back(interpretation);
    }

    cout << "\nТаблиця істинності:" << endl;
    cout << string(num_variables * 5 + expression.length() + 4, '-') << endl;
    cout << "|";
    for (int i = 0; i < num_variables; ++i) {
        cout << " " << variables[i] << " |";
    }
    cout << " " << expression << " |" << endl;
    cout << string(num_variables * 5 + expression.length() + 4, '-') << endl;
    
    for (vector<bool>& interpretation : interpretations) {
        cout << "|";
        for (bool& value : interpretation) {
            cout << " " << value << " |";
        }
        cout << "  " << evaluate(expression, interpretation) << "  |" << endl;
        cout << string(num_variables * 5 + expression.length() + 4, '-') << endl;
    }

    return 0;
}