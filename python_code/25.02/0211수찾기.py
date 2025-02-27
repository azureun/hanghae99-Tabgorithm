def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    # 이진 탐색이 계속 실행될 조간
    while (left<=right):      #이진탐색 : 왼쪽 인덱스 & 오른쪽 인덱스 사이 범위 좁혀가며 진행. 종료하려면 left가 right보다 커야 함.
        mid = (left + right) // 2

        if arr[mid] == target:     # 이진 탐색에서 타겟을 찾았는지 확인하는 조건
            return True
        elif (arr[mid] < target):   # 타겟 값이 중간 값보다 큰 경우의 조건
            left = mid + 1  # 오른쪽 부분 탐색
        else:
            right = mid - 1 # 왼쪽 부분 탐색
    return False

# 입력 처리
N = int(input().strip())    # 배열 크기 입력
A = list(map(int, input().strip().split()))
M = int(input().strip())    # 질의 개수 입력
queries = list(map(int, input().strip().split()))

# 이진 탐색을 위해 정렬
A.sort()

# 이진 탐색을 통한 결과 계산
results = []
for query in queries:
    if binary_search(A, query):
        results.append(1)
    else:
        results.append(0)

# 결과 출력
for results in results:
    print(results)

