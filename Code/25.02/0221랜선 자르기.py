def find_max_length(K, N, cables):  
    start = 1
    end = max(cables)       # 케이블 중 최대 길이가 end

    while start <= end:     # start가 end길이만큼 도달할 때까지 반복
        mid = (start + end) // 2  # 중간값 계산

        # 현재 길이로 만들 수 있는 랜선의 개수 계산
        count = 0  # 각 케이블에서 만들 수 있는 랜선 수의 합
        for cable in cables:
            count += cable // mid   # 케이블 길이를 중간값으로 나눔

        if count >= N:  # 랜선을 N개 이상 만들 수 있는 경우
            start = mid + 1  # 더 긴 길이 시도
        else:           # 랜선을 N개 이상 만들 수 없는 경우
            end = mid - 1   # 더 짧은 길이 시도

    return end

# 입력 처리
K, N = map(int, input().split())    # 현재 가지고 있는 랜선 수, 필요한 랜선 수
cables = [int(input()) for _ in range(K)]   # K개의 줄에 걸쳐 [랜선 길이] 입력
print(find_max_length(K, N, cables))