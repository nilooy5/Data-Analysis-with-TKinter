import utility as util

number = 3.51

end = util.round_to_closest_int(number)

arr = list(range(1, end + 1))
arr = arr[::-1]
# print(arr)

i = 0

while i != len(arr):
    for j in range(i, len(arr)):
        print(arr[j], end= ' ')
    print()
    i = i + 1
