def fill_box(l, w, h, blocks):
    blocks.sort(reverse=True, key=lambda x: x[0])  # 블록 크기 순서대로 정렬
    total_count = 0
    volume = l * w * h  # 상자의 전체 부피
    used_volume = 0     # 이전 단계에서 사용한 블록 개수

    for i in range(len(blocks)):
        size = 2 ** blocks[i][0]  # 블록의 한 변 길이 > blocks[i][0]은 블록 크기를 $2^k$로 표현한 지수 값.
        count = blocks[i][1]  # 사용 가능한 블록 개수

        if volume <= used_volume:
            break  # 상자를 이미 채웠다면 종료

        max_count = (l//size) * (w//size) * (h//size)  # 현재 크기로 채울 수 있는 최대 개수 > 각 차원에서 해당 블록 크기로 몇 개가 들어갈 수 있는지 계산한 값의 곱.
        
        # 사용 가능한 개수만큼 배치
        use_count = min(count, max_count)
        total_count += use_count
        max_count -= used_volume // (size ** 3)  # 이미 채워진 공간 제외
        used_volume += use_count    # 현재 크기 블록 > 사용한 개수 업데이트

        # 남은 공간 업데이트
        volume -= use_count * (size ** 3)  # 상자 전체 부피 업데이트 > 채워진 공간 만큼 전체 상자 크기 줄어듦.

        # 상자를 다 채웠는지 확인
        if volume == 0:
            return total_count  # 채운 상자 개수 리턴
        
    return -1   # 공간이 남으면 채울 수 없으므로 -1 리턴

# 입력
l, w, h = map(int, input().strip().split())
n = int(input().strip())
blocks = [tuple(map(int, input().strip().split()))
          for _ in range(n)]

# 출력
print(fill_box(l, w, h, blocks))
