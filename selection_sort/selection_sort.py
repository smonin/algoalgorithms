my_arr = [3, 1, 4, 10, -28, 7, 25, 9, 0, 28, 111, 87, 239]
print("Unsorted array:")
print(my_arr)

for i in range(len(my_arr) - 1):
    min_index = i
    for j in range(i + 1, len(my_arr)):
        if my_arr[j] < my_arr[min_index]:
            min_index = j
    my_arr[i], my_arr[min_index] = my_arr[min_index], my_arr[i]

print(my_arr)