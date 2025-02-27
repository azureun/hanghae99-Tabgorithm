from bisect import bisect_left  # bisect : 이진탐색 라이브러리

def min_removals_to_sort(n, cards):
    lis = []  # LIS (Longest Increasing Subsequence) : 최장 증가 부분 수열
    for card in cards:
        pos = bisect_left(lis, card)  # LIS 위치 찾기
        if pos == len(lis):
            lis.append(card)        # 오름차순 정렬된 것 배열에 추가
        else:
            lis[pos] = card  # LIS 값 갱신
    return n - len(lis)  # 최소 제거 카드 수 계산

# 입력 처리
N = int(input())                    # 전체 카드 길이
A = list(map(int, input().split())) # 숫자 카드 입력
print(min_removals_to_sort(N, A))   

# 6 1 2 3 2 4 5 10 이면 6, 2, 10 제거 -> 출력 : 3
