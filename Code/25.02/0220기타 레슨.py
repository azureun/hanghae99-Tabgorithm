def can_record(lessons, m, size):
    count = 1
    current_sum = 0

    for lesson in lessons:
        if lesson > size:
            return False
        if current_sum + lesson > size:
            count += 1
            current_sum = ____  # 새로운 블루레이에 현재 강의 추가
        current_sum += lesson

    return count ____  # 필요한 블루레이 개수 확인

def min_bluray_size(n, m, lessons):
    left = ____  # 가능한 최소 크기
    right = sum(lessons)
    result = right

    while left <= right:
        mid = (left + right) // 2
        if can_record(lessons, m, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

# 입력 처리
N, M = map(int, input().split())
lessons = list(map(int, input().split()))
print(min_bluray_size(N, M, lessons))