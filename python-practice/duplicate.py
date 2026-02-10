data = [1,2,4,2,5,6,7,3,5,1]

#time complexity O(n2)

# duplicate = [x for x in data if data.count(x) > 1]
# print(duplicate)


#time complexity O(n)

seen = set()
duplicate = set()

for x in data:
    if x in seen:
        duplicate.add(x)
    else:
        seen.add(x)

print(seen)
print(duplicate)