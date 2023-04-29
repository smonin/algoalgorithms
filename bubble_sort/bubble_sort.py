my_arr = [3, 1, 4, 10, 7, 25, 9, 28, 111, 87, 239]
print("Unsorted array:")
print(my_arr)

my_arr_len = len(my_arr)

count = 0

for attempt in range(my_arr_len-1):
    for i in range(my_arr_len-1):
        if my_arr[i] > my_arr[i+1]:
            count += 1
            my_arr[i], my_arr[i+1] = my_arr[i+1], my_arr[i]

print("Amount of attempts: " + str(count))
print("Sorted array:")
print(my_arr)