def two_pointers(a, b):
    n = len(a)
    m = len(b)
    i = 0
    j = 0
    while i < n and j < m - 1:   
        if a[i] == b[j]:
            return True
        elif a[i] < b[j]:
            i = i + 1
        else:
            j = j + 1
    return True                  

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(two_pointers(a, b))