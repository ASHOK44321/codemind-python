
def print_pattern(N):
    for i in range(1, N + 1):
        print((str(i) + ' ') * N, end='
')
N = int(input())
print_pattern(N)
