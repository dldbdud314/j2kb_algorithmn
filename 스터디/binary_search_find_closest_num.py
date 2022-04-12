#not_leet_code

def binary_search_find_closest_num(array, target):
    left = 0
    right = len(array) - 1
    
    min_interval = float('inf')
    element = 0
    while left <= right:
        mid = (left + right) // 2
        interval = abs(target - array[mid])
        if min_interval > interval:
            min_interval = interval
            element = array[mid]
        
        if target > array[mid]:
            left = mid + 1
        elif target < array[mid]:
            right = mid - 1
            
    return element

print(binary_search_find_closest_num([1, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 17, 99, 100, 101, 189], 95))