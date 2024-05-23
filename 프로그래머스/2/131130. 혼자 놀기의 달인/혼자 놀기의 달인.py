def solution(cards):
    def dfs_box(start, visited, cards):
        size = 0
        while not visited[start]:
            visited[start] = True
            start = cards[start] - 1
            size += 1
        return size

    visited = [False] * len(cards)
    box_s = []

    for i in range(len(cards)):
        if not visited[i]:
            group_size = dfs_box(i, visited, cards)
            box_s.append(group_size)

    if len(box_s) < 2:
        return 0

    box_s.sort(reverse=True)
    return box_s[0] * box_s[1]