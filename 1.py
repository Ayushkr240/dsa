# def bubblesort(arr):
#     n=len(arr)
#     for i in range(1,n):
#         for j in range (0,n-1):
#             if (arr[j]>arr[j+1]):
#                 arr[j],arr[j+1]=arr[j+1],arr[j]

#     return arr

# arr=[23,53,2,88,56]
# print("original list ",arr)
# arr=bubblesort(arr)
# print("Final list ",arr)


def bubble_sort(arr):
    n=len(arr)

    for i in range(1,n):
        for j in range(0,n-1):
            if (arr[j]>arr[j+1]):
                arr[j], arr[j+1]=arr[j+1],arr[j]

    return arr

arr=[23,53,2,88,56]
print("original list ",arr)
arr=bubble_sort(arr)
print("Final list ",arr)