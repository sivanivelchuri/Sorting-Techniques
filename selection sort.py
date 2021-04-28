n=7
arr=[9,3,1,4,2,7,5]
for i in range(0,n-1):
    minimum=i
    for j in range(i+1,n):
        if arr[j]<arr[minimum]:
            minimum=j
    temp=arr[i]
    arr[i]=arr[minimum]
    arr[minimum]=temp
print(arr)
