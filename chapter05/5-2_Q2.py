min = 2
max = 10
total = 100
memo = {}

def problem(rest, sit):
    key = str([rest, sit])

    if key in memo:
        return memo[key]
    if rest < 0:
        return 0
    if rest == 0:
        return 1

    # recursion
    count = 0
    for i in range(sit, max+1):
        count += problem(rest-i, i)
    # memoization
    memo[key] = count
    # exit
    return  count

print(problem(total, min))