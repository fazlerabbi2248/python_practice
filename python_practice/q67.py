def binarysearch(arr,search):
    lower =0
    l = len(arr)

    while(l>lower):
        mid = int((lower+l)/2)
        print(mid)
        if(arr[mid]==search):
            return mid
        elif(search < arr[mid]):
            l =mid

        elif(search>arr[mid]):
            lower = mid+1


ar = [1,2,4,6,8,65,76,23,67,89,100]
search = 6
print(binarysearch(ar,search))

