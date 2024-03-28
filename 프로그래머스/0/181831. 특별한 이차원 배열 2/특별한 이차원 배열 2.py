def solution(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):  # 대각선을 기준으로 한 쪽만 검사하면 됨
            if arr[i][j] != arr[j][i]:
                return 0
    return 1