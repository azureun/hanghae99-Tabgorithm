def count_coin_cases(n, k, coins):
    dp = [0] * (k + 1)
    dp[0] = 1  # 초기값 설정 > 동전을 선택하지 않는 경우 또한 1개의 경우 이므로 추가

    for coin in coins:
        for j in range(coin, k + 1):    #j : 현재 금액 / coin : 현재 동전 가치
            dp[j] += dp[j-coin]  # 현재 동전을 사용하는 경우의 수 추가

    return dp[k]  # 최종 결과 반환

# 입력 처리
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
print(count_coin_cases(n, k, coins))