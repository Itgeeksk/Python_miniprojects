# Navie Search method 

def navie_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i 
    return -1

result = navie_search([1,2,5,4,8,6] , 1)
print("Element index is :" , result)


# Binary Search approch RECURSIVE METHOD

def binary_search(arr , x, low , high):
    if high >= low:
        midp = (low + high) // 2
        if arr[midp] == x:
            return midp
        elif arr[midp] > x:
            return binary_search(arr , x , low , midp - 1)
        else:
            return binary_search(arr  , x , midp + 1 , high )
    else:
        return -1


arr = [2, 3, 4, 10, 40, 50, 60, 65, 100, 105, 125, 185, 210, 250]
x = 185

ans = binary_search(arr , x , 0 , len(arr)-1)
if ans != -1:
    print("Element is present at index no:" ,str(ans))
else:
    print("Element is not present in arr")

def binary_it(arr , x):

    low = 0
    high = len(arr) -1 
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1


arr = [2, 3, 4, 10, 40, 50, 60, 56, 100, 105, 125, 185, 210, 250]
x = 100
result = binary_it(arr , x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")