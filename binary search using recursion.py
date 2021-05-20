def binary_search(arr,l,h,n):
    if h>=l:
        m=(l+h)//2
        if arr[m]==n:
            return m
        elif arr[m]>n:
            return binary_search(arr,l,m-1,n)
        else:
            return binary_search(arr,m+1,h,n)
    else:
        return -1
arr=[1,3,5,8,6,9]
n=5
ans=binary_search(arr,0,len(arr)-1,n)
if ans!=-1:
    print("present",arr[ans])
else:
    print("not present")
