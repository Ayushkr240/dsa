
# def mergeSort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2

#         left = arr[:mid]
#         right = arr[mid:]

#         mergeSort(left)
#         mergeSort(right)

#         i = j = k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 arr[k] = left[i]
#                 i += 1
#             else:
#                 arr[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             arr[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             arr[k] = right[j]
#             j += 1
#             k += 1

#     return arr


# arr = [38, 27, 43, 3, 9, 82, 10]

# print("Original array:", arr)
# mergeSort(arr)
# print("Sorted array:", arr)

def merge_sort(arr):

    n=len(arr)
    if len(arr)<=1:
        return arr
    mid=n//2

    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])

    i=j=k=0

    while i < len(left) and j <len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1

    # 
    while i <len(left):
        arr[k]=left[i]
        i+=1
        k+=1

    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1

    return arr


arr = [38, 27, 43, 3, 9, 82, 10]

print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)
