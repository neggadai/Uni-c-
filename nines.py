def split_number(number,num_len):
    num_mass = []
    s = number
    for i in range(num_len):
        num_mass.append(s % 10 * (10**i))
        s = s//10
    return num_mass
    

def max_number(length):
    previous = 0
    current = 0
    for i in range(length):
        current = previous*10 + 10**i
        previous = current
    return current

def count_nines(n):
    length = len(str(n))
    mass = split_number(n,length)
    num_count = 0
    prev = 1

    for i in range(length):
        current_part = mass[i]
        high_bit = current_part//(10**(i))
        num_count += high_bit*max_number(i)
        if high_bit == 9:
            num_count += prev
    return num_count