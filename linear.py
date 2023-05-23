def linear_search_recursive(arr, target, index=0):
    
    if index == len(arr):
        return -1
    
    if arr[index] == target:
        return index
    else:
        return linear_search_recursive(arr, target, index + 1)
    
    
arr = [1, 3, 5, 7, 9, 11]
target = 5

result = linear_search_recursive(arr, target)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")