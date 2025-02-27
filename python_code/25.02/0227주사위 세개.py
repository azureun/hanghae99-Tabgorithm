# 주사위 눈 입력
a, b, c = map(int, input().split())

# 상금 계산
def compute_prize(a, b, c):
    if a == b == c:             # 3개 모두 같은 숫자
        return 10000 + a * 1000
    elif a==b or a==c or b==c:  # 2개만 같은 숫자
        if a == b or a == c:    # a와 b가 같거나 a와 c가 같을 때
            return 1000 + a * 100
        else:                   # 아닐땐 b로 계산
            return 1000 + b * 100
    else:       # 가장 큰 눈 수로 계산
        return max(a, b, c) * 100

# 결과 출력
prize = compute_prize(a, b, c)
print(prize)

