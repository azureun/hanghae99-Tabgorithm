def merge_sort(arr, temp, left, right):
    # 병합 정렬의 종료 조건을 나타내는 코드, 배열의 크기가 1이하인 경우
    if left >= right:   # 배열 크기가 1이하이면 종료
        return 0
    
    mid = (left + right) // 2
    inv_count = 0

    # 왼쪽과 오른쪽을 나누어 정렬하고 swap 횟수를 계산
    inv_count += merge_sort(arr, temp, left, mid)       # 왼쪽 정렬
    inv_count += merge_sort(arr, temp, mid + 1, right)  # 오른쪽 정렬
    inv_count += merge(arr, temp, left, mid, right)     # 병합 & swap 횟수

    return inv_count

def merge(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0 

    # 병합 과정에서 swap 횟수 계산
    while i <= mid and j <= right:
         # 왼쪽 배열과 오른쪽 배열의 요소를 비교하여 작은 값을 temp 배열에 삽입하기 위한 조건
        if arr[i] <= arr[j]:   # 왼쪽 배열 작거나 같으면 temp에 저장
             temp[k] = arr[i]
             i += 1
        else:
            temp[k] = arr[j]    # 오른쪽 배열 작다면, 왼쪽 남은 요소만큼 swap
            j += 1
            inv_count += (mid - i + 1)  # 남아있는 왼쪽 배열 요소 개수만큼 swap 발생
        k += 1
    
    # 남아있는 요소들을 병합
    while i <= mid:
         temp[k] = arr[i]
         i += 1
         k += 1
    
    while j <= right:
         temp[k] = arr[j]
         j += 1
         k += 1
    
    # temp의 내용을 원래 배열로 복사
    for i in range(left, right + 1):
         arr[i] = temp[i]
        
    return inv_count

# 입력
n = int(input().strip()) # 정수로 변환
arr = list(map(int, input().strip().split()))     # 리스트 입력

temp = [0] * n
# 출력
print(merge_sort(arr, temp, 0, n-1)) # 횟수 출력

