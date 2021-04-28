a=[11,34,55,100,110,19,12,60,18,16]
for i in range(1,len(a)):
    key=a[i]
    j=i-1
    while j>=0 and a[j]>key:
        a[j+1]=a[j]
        j-=1
    a[j+1]=key
print(a)
