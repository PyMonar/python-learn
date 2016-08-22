# Sort collection

def select(arr):
    '''Select sort'''
    for i in range(0, len(arr)):
        min = i
        for j in range(i, len(arr)):
            min = j if arr[j] < arr[min] else min
        arr[i], arr[min] = arr[min], arr[i]

def insert(arr):
    '''Insert sort'''
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break

arr = [6, 9, 1, 4, 2, 5, 7, 0, 8, 3, -1, 27, 13, -17]
#select(arr)
insert(arr)
print arr