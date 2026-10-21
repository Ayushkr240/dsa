# def binary_search(arr,low,high,x):
#     N = len(arr)

#     mid=(low+high)//2

#     if (arr[mid]==x):
#         return mid
#     elif (x<arr[mid]):
#         binary_search(arr,low,mid-1,x)

#     else :
#         binary_search(arr,mid+1,high,x)

  
def binary_search(arr,x,low,high):
    if low>high:
        return -1
    mid=(low+high)//2

    if arr[mid]==x:
        return mid

    elif x<arr[mid]:
        return binary_search(arr,x,low,mid-1)

    else:
        return binary_search(arr,x,mid+1,high)

arr=[1,3,5,6,8]
index=binary_search(arr,6,0,len(arr)-1)

if index != -1:
    print("Element found at index:",index)
else:
    print("Element not found")
    


