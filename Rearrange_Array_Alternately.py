def rearrange_alternatively(arr, n):
    max_idx = n - 1
    min_idx = 0
    max_elem = arr[max_idx] + 1

    for i in range(n):
        if i % 2 == 0:
            arr[i] += (arr[max_idx] % max_elem) * max_elem
            max_idx -= 1
        else:
            arr[i] += (arr[min_idx] % max_elem) * max_elem
            min_idx += 1
    for i in range(n):
        arr[i] = arr[i] // max_elem

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    rearrange_alternatively(arr, N)
    print(*arr)
