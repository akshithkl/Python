def find_max(arr, left, right):
    if left == right:
        return arr[left]
    
   
    mid = (left + right) // 2

 
    max_left = find_max(arr, left, mid)
    max_right = find_max(arr, mid + 1, right)

 
    return max(max_left, max_right)


array = [3, 1, 4, 1, 5, 9, 2, 6]
result = find_max(array, 0, len(array) - 1)
print(f"The maximum number in the array is: {result}")
