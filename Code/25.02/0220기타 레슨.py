def can_record(lessons, m, size):
    count = 1           # 필요한 블루레이 개수 카운트
    current_sum = 0     # 현재 강의 개수 합

    for lesson in lessons:
        if lesson > size:
            return False
        if current_sum + lesson > size:
            count += 1
            current_sum = 0  # 새로운 블루레이에 현재 강의 추가
            # 새로운 블루레이 시작하려면 0으로 초기화한 후,
        current_sum += lesson   # 현재 강의인 lesson이 더해짐.

    return count <= m  # 필요한 블루레이 개수 확인

def min_bluray_size(n, m, lessons):
    left = max(lessons)     # 가능한 최소 크기 : 가장 긴 강의 시간
    right = sum(lessons)    # 가능한 최대 크기 : 모든 강의를 한 블루레이에 넣을 경우
    result = right          # 최소 블루레이 크기 저장 right(최대 크기에서 시작함.)

    while left <= right:            # left가 right 보다 작거나 같을 때까지 반복
        mid = (left + right) // 2   # 중간 값 : 현재 블루레이 크기 후보 값
        if can_record(lessons, m, mid): # mid 크기 블루레이로 m개 이하의 블루레이에 모든 강의 담을 수 있으면
            result = mid        # 블루레이를 결과에 저장
            right = mid - 1     # 더 작은 블루레이도 가능한지 확인
        else:                       # mid 크기에 담기 어려우면
            left = mid + 1          # mid 크기 늘리기

    return result

# 입력 처리
N, M = map(int, input().split())
lessons = list(map(int, input().split()))
print(min_bluray_size(N, M, lessons))