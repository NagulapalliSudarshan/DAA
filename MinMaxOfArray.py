def MaxMin(a,l,r,Max,Min):
    if l==r:
        Max = a[l] 
        Min = a[l]
    elif l==r-1:
        if a[l]>a[r]:
            Max = a[l]
            Min = a[r]
        else:
            Max = a[r]
            Min = a[l]
    else:
        mid = (l+r)//2
        max1,min1 = MaxMin(a,l,mid,Max,Min)
        max2,min2 = MaxMin(a,mid+1,r,Max,Min)
        if max1>max2:
            Max = max1
        else:
            Max = max2
        if min1<min2:
            Min = min1
        else:
            Min = min2
        
    return Max,Min

print("Enter the elements of the array : ")
arr = [int(x) if x.isnumeric() else x for x in input().split()] 
print(MaxMin(arr,0,len(arr)-1,float('-inf'),float('inf')))