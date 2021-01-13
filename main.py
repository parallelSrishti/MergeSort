#Python3


def mergeSort(arr, l, r):
    if l<r:
        # Finding the mid of the array
        m = (l+r)//2

        # Sorting the first half
        mergeSort(arr, l, m)

        # Sorting the second half
        mergeSort(arr, m+1, r)

        #merging the two halves
        merge(arr, l, m, r)
def merge(arr, l, m, r):
    l1 = m-l+1
    l2 = r-m

    # Copy data to temp arrays L[] and R[]
    L = [0]*l1
    R = [0]*l2
    for i in range (0, l1):
        L[i] = arr[l+i]
    for j in range(0, l2):
        R[j] = arr[m+1+j]
    i = j = 0
    k=l
    while i<l1 and j<l2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1
    # Checking if any element was left
    while i < l1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < l2:
        arr[k] = R[j]
        j += 1
        k += 1


# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr, 0, len(arr)-1)
    print("Sorted array is: ", end="\n")
    printList(arr)
