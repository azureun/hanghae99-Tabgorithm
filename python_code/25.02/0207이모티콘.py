def min_time_to_make_emoticons(S):
    # 현재 이모티콘 수, 클립보드의 이모티콘 수, 소요 시간을 저장
    visited = set()
    queue = [(1, 0, 0)]
    visited.add((1,0))

    while queue:
        screen, clipboard, time = queue.pop(0)

        if screen == S:
            return time
        #현재 화면의 이모티콘을 클립보드에 복사
        if (screen, screen) not in visited:
            visited.add((screen, screen))   #add(1, 0)
            queue.append((screen, screen, time + 1))
        # 클립보드의 이모티콘을 화면에 붙여넣기
        if clipboard > 0 and (screen + clipboard) not in visited:
            visited.add((screen + clipboard, clipboard))
            queue.append((screen + clipboard, clipboard, time + 1))
        # 이모티콘 하나를 삭제
        if screen > 0 and (screen - 1, clipboard) not in visited:
            visited.add((screen-1, clipboard))
            queue.append((screen-1, clipboard, time + 1))

# 입력 처리
S = int(input())
print(min_time_to_make_emoticons(S))
