a = input()
count = 0 

if a%2 == 0:
    while a != 0:
        a = a-2
        count += 1
else:   
    a = a - 9
    count += 2 
    while a != 0:
        a = a-2
        count += 1
