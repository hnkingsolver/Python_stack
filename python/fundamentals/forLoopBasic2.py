#big size
def biggie_size(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = "big"
    print (arr)
biggie_size([-1,3,5,-5])

def count_positives(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            count += 1
    arr[-1] = count
    print (arr)
count_positives([-1,-1,1,1,1])

def sumTotal(arr):
    sum=0
    for i in range(len(arr)):
        sum+= arr[i]
    print(sum)
    return sum
sumTotal([1,3,5,1])

def average(arr):
    sum = 0
    avg = 0
    for i in range(len(arr)):
        sum += arr[i]
        avg = sum/len(arr)
    print(avg)
    return avg
average([1,2,3,4])

def length(arr):
    count=0
    for i in range (len(arr)):
        count += 1
    print(count)
    return count
length([1,2,3,4])

def minimum(arr):
    min = arr[0]
    if len(arr) == 0:
        return False
    for i in arr:
        if i < min:
            min = i
    print(min)
    return min
minimum([-20,1,2,3])

def maximum(arr):
    max = arr[0]
    if len(arr)==0:
        return False
    for i in arr:
        if i > max:
            max=i
    print(max)
    return max
maximum([1,2,3,4])

def ultimate_analyze(arr):
    dict = {
        'sum' : sumTotal(arr),
        'avg' : average(arr),
        'min' : minimum(arr),
        'max' : maximum(arr),
        'len' : length(arr)
    }
    print(dict)
    return dict
ultimate_analyze([1,2,3,20])

def reversed(arr):
    arr = arr[::-1]
    print(arr)
    return arr
reversed([1,2,3,4])