# def insertion_sort(arr):
#     n=len(arr)
#     for i in range(n-1):
#         for j in range(i+1,0,-1):
#             if (arr[j]<arr[j-1]):
#                 arr[j],arr[j-1]=arr[j-1],arr[j]

#     return arr
            

def insertion_sort(arr):
    n=len(arr)

    for i in range(n-1):
        for j in range(i+1,0,-1):
            if (arr[j-1]>arr[j]):
                arr[j],arr[j-1]=arr[j-1],arr[j]
    return arr


arr=[23,53,2,88,56]
print("original list ",arr)
arr=insertion_sort(arr)
print("Final list ",arr)