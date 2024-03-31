A = {1, 2, 3, 4, 5, 6, 7}
B = {4, 5, 6, 7, 8, 9, 10}
C = {1, 3, 5, 7, 9}
U = {i for i in range(1, 11)}  

# a) Обчислення A ∪ ¬(B ∩ C)
result_a = A.union(U - (B.intersection(C)))

# б) Обчислення (A\C)∆B
result_b = (A - C).symmetric_difference(B)

# Виведення результатів
print("Множина A ∪ ¬(B ∩ C):", result_a)
print("Множина (A\C)∆B:", result_b)
