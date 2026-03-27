def binary(arr,target,low,high):
    if low > high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binary(arr,target,low,mid-1)
    else:
        return binary(arr,target,mid+1,high)
arr=[10,20,30,40,50]
target=30
print(binary(arr,target,0,len(arr)-1))