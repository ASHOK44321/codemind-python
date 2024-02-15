def record_breaking_days(test_cases):
    results = []

    for idx, test_case in enumerate(test_cases, 1):
        N, visitors = test_case
        record_breaking_count = 0
        max_visitors = -1

        for i in range(N):
            if visitors[i] > max_visitors and (i == N - 1 or visitors[i] > visitors[i + 1]):
                record_breaking_count += 1

            max_visitors = max(max_visitors, visitors[i])

        results.append((idx, record_breaking_count))

    return results
T = int(input())
test_cases = []

for _ in range(T):
    N = int(input())
    visitors = list(map(int, input().split()))
    test_cases.append((N, visitors))
results = record_breaking_days(test_cases)

for idx, count in results:
    print(f"Case #{idx}: {count}")
