def intersection(set1, set2):
    intersect = []
    for elem in set1:
        if elem in set2:
            intersect.append(elem)
    return intersect

def union(set1, set2):
    union_set = set1.copy()
    for elem in set2:
        if elem not in union_set:
            union_set.append(elem)
    return union_set

def main():
    print("Введіть першу множину:")
    set1 = input("Елементи розділені пробілами: ").split()
    print("Введіть другу множину:")
    set2 = input("Елементи розділені пробілами: ").split()

    set1 = list(map(float, set1))
    set2 = list(map(float, set2))

    intersect = intersection(set1, set2)
    union_set = union(set1, set2)

    print("Переріз множин:", intersect)
    print("Об'єднання множин:", union_set)

    print("Потужність перерізу множин:", len(intersect))
    print("Потужність об'єднання множин:", len(union_set))

if __name__ == "__main__":
    main()
