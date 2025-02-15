from bisect import bisect_left

def min_removals_to_sort(n, cards):
    lis = []  # LIS (Longest Increasing Subsequence) : 최장 증가 부분 수열
    for card in cards:
        pos = bisect_left(lis, card)  # LIS 위치 찾기
        if pos == len(lis):
            lis.append(card)
        else:
            lis[pos] = card  # LIS 값 갱신
    return n - len(lis)  # 최소 제거 카드 수 계산

# 입력 처리
N = int(input())
A = list(map(int, input().split()))
print(min_removals_to_sort(N, A))

