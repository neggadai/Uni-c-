
def intersect(set1,set2):
    inter = []
    for i in set1:
        for g in set2:
            if g == i:
                inter.append(g)
    return inter

def diff(set1,set2):
    differ = []
    for i in set1:
        IsInSet1 = False
        for g in set2:
            if g == i:
                IsInSet1 = True
        if not IsInSet1:
            differ.append(i)
    return differ


set1 = input("Введіть першу множину: ").split()

#for i in set1:
#    assert type(i) == float or i == " ", "wrong_type"

set2 = input("Введіть другу множину: ").split()
#for i in set2:
#    assert type(i) == float or i == " ", "wrong_type"

intersection = intersect(set1,set2)
difference = diff(set1,set2)

print("Переріз множин:", intersection)
print("Різниця множин:", difference)

print("Потужність перерізу множин:", len(intersection))
print("Потужність різниці множин:", len(difference))

