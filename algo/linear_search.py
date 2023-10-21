def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Element found, return its index
    return -1  # Element is not in the array

# Example usage:
my_list = [11, 12, 22, 25, 34, 64, 90]
target = 25
result = linear_search(my_list, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
