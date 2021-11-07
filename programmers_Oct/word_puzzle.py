import sys
def solution(strs, t):
    strs = set(strs)
    dp = [sys.maxsize for i in range(len(t)+1)]
    dp[0] = 0
    for i in range(1,len(t)+1):
        j = i - 5 if i > 5 else 0
        while j < i:
            if dp[j] + 1 < dp[i] and t[j:i] in strs:
                dp[i] = dp[j]+1
            j += 1

    return dp[len(t)] if dp[len(t)] != sys.maxsize else -1

print(solution(["ba","na","n","a"], "banana"))
print(solution(["app","ap","p","l","e","ple","pp"]	, "apple"))
print(solution(["ba","an","nan","ban","n"], "banana"))
