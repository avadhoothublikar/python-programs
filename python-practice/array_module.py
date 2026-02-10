#import array as arr
from array import *

# val = array('i', [1,2,3,4,5,6,7,8])

# for i in range(0,len(val)):
#     print(val[i], end=" ")

# print('\n')

# for x in val:
#     print(x, end=" , ")

# print('\n')

# print(val.typecode)

# val.reverse()

# val.insert(1,50)
# val.append(20)
# val[2] = 60

# copyArr = array(val.typecode, (x*2 for x in val) )

# # abc = val[2:-2]

# # reverseing array
# abc = val[::-1]

# for i in range(0, len(abc)):
#     print(abc[i], end=" ")

arr = array('i', [])
n = int(input("enter the size of array: "))

for i in range(0,n):
    arr.append(int(input("enter next num ")))

search_arr = arr.index(12)
print(search_arr)

for x in arr:
    print(x, end= " ")
