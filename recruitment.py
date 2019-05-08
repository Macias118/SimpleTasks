def generate_postcodes():
    s1 = "79-900"
    s2 = "80-155"
    res = []
    for i in range(int(s1.split('-')[1])+1, 999):
        res.append('79-{}'.format(i))
    for j in range(1, int(s2.split('-')[1])):
        res.append('80-{:03d}'.format(j))
    return res

def get_missing_elements(array, n):
    return [i for i in range(n + 1) if i not in array]

def semi_jump():
    from decimal import *
    return [Decimal(i) / Decimal(2) for i in range(4, 12)]
