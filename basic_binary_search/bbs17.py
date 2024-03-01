def binary_search_recursive(arr, target, low, high):
    # Base case: element not found
    if low > high:
        return -1  

    mid = (low + high) // 2

    if arr[mid] == target:
        # Base case: element found at mid index
        return mid  
    elif arr[mid] > target:
        # Search left half
        return binary_search_recursive(arr, target, low, mid - 1)  
    else:
        # Search right half
        return binary_search_recursive(arr, target, mid + 1, high)  


# Example usage:
arr = [101, 444, 567, 812, 999, 1101, 1232, 1522, 1684, 1789, 1893, 1998, 2145, 3469, 4563, 5456, 6777, 6985, 7854, 8792, 9687,10002,]
target = 1101
result = binary_search_recursive(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Element: {target} which also can be referred to as: {arr[result]} found at index: {result}")
else:
    print("Element not found.")