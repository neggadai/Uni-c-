import itertools

A = {1, 2, 3, 4, 5, 6, 7}
B = {4, 5, 6, 7, 8, 9, 10}
C = {1, 3, 5, 7, 9}
U = {i for i in range(1, 11)}  

result_a = A.intersection((U - B).symmetric_difference(C))

bolean = []
for i in range(len(result_a)+1):

    bolean.append(itertools.combinations(result_a,i))

def iter_to_value(iterator,arr):
    try:
        while True:
            next_val = next(iterator)
            arr.append(next_val)
    except StopIteration:
        pass

bolean_answer = []
for i in bolean:
    iter_to_value(i,bolean_answer)

print(f"Булеан: {bolean_answer}")
print(f"Потужність булеану = {len(bolean_answer)}")