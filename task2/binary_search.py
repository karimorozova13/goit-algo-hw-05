
def binary_search(arr,target):
    low = 0
    high = len(arr) - 1
    mid = 0
    count = 1
    while low <= high:
        
        count += 1
        mid = (high + low) // 2
        
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return (count, arr[mid])
  
    if low > 0 and (low != len(arr) or abs(arr[low] - target) <= abs(arr[low - 1] - target)):
       return (count, arr[low])
   

numbers = [1.2, 2.0, 3.5, 4.1, 5.7, 6.3, 7.8, 8.2, 9.4, 10.0]
print(binary_search(numbers, 3.6))