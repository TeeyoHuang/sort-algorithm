
def SelectSort(arr):
    for i in range(len(arr)-1):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[minIndex]:
                minIndex=j
        if(minIndex!=i):
            arr[minIndex],arr[i] = arr[i], arr[minIndex]

def InsertSort(arr):
    for i in range(len(arr)):
        for j in range(i-1, -1, -1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def BubbleSort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def ShellSort(arr):
    gap_list=[5,3,1,0]
    k=0
    while(gap_list[k]>0):
        gap=gap_list[k]
        for i in range(gap,len(arr)):
            for j in range(i-gap, -1, -1):
                if arr[j]>arr[j+gap]:
                    arr[j], arr[j+gap]= arr[j+gap], arr[j]
        k+=1

def QuickSort(arr, L, R):
    if(L>=R):
        return

    i, j, key = L, R, L

    while(i<j):
        while i<j and arr[key]<arr[j]:
            j-=1
        if i<j:
            arr[key], arr[j] = arr[j], arr[key]
            key = j
            i+=1

        while i<j and arr[key]>arr[i]:
            i+=1
        if i<j:
            arr[key], arr[i] = arr[i], arr[j]
            key = i
            j-=1

    QuickSort(arr, L, key)
    QuickSort(arr, key+1, R)

def MergeSort(arr, L, R):
    if(L>=R):
        return

    M = L+(R-L)//2

    MergeSort(arr, L, M)
    MergeSort(arr, M+1, R)

    help_list=[]
    p1, p2 = L, M+1

    while(p1<=M and p2<=R):
        if arr[p1]<arr[p2]:
            help_list.append(arr[p1])
            p1+=1
        else:
            help_list.append(arr[p2])
            p2+=1

    while(p1<=M):
        help_list.append(arr[p1])
        p1+=1
    while(p2<=R):
        help_list.append(arr[p2])
        p2+=1

    for k in range(len(help_list)):
        arr[L+k]=help_list[k]


def heapify(arr, i, heapsize):
    left, right = 2*i+1, 2*i+2
    largest=i
    if left <=heapsize and arr[left] > arr[largest]:
        largest = left
    if right <=heapsize and arr[right] >arr[largest]:
        largest = right

    if(largest!=i):
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, heapsize)

def HeapSort(arr):

    for i in range(len(arr)//2-1, -1, -1):
        heapify(arr, i, len(arr)-1)

    for j in range(len(arr)-1, 0, -1):
        arr[0], arr[j] = arr[j], arr[0]
        heapify(arr, 0, j-1)

def CountingSort(arr):
    max_value=max(arr)

    help_list=[0]*(max_value+1)
    for i in range(len(arr)):
        help_list[arr[i]]+=1

    n=0
    for k in range(len(help_list)):
        while help_list[k] > 0:
            arr[n]=k
            n += 1
            help_list[k]-=1

def RadixSort(arr):
    max_value=max(arr)
    d=0
    while max_value >0:
        d+=1
        max_value//=10

    radix=1
    count_list=[0]*10
    for i in range(d):
        count_list = [0]*10 #计数器置零

        for j in range(len(arr)):
            k=arr[j]//radix % 10
            count_list[k]+=1

        for n in range(1,10):
            count_list[n] = count_list[n]+count_list[n-1]

        list_temp=[0]*len(arr)

        for m in range(len(arr)-1, -1, -1):
            k=arr[m]//radix % 10
            list_temp[count_list[k]-1]=arr[m]
            count_list[k]-=1

        for i in range(len(arr)):
            arr[i]=list_temp[i]

        radix*=10
