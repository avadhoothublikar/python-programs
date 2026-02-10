unsorted = [2,5,2,7, 9, 10, 1, 0]

sorted = []

while unsorted:
    min = unsorted[0]
    for x in unsorted:
        if x < min:
            min = x
    sorted.append(min)
    unsorted.remove(min)

print(sorted)