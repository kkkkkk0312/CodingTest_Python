def solution(numbers, target):
    def dfs(index, s_num):
        if index==len(numbers):
            if s_num==target:
                return 1
            else:
                return 0
        return dfs(index+1, s_num+numbers[index]) + dfs(index+1, s_num-numbers[index])
    return dfs(0,0)