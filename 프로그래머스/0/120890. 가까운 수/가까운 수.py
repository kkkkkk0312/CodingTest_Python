def solution(array, n):
    array.append(n)
    array.sort()
    index_n=array.index(n)
    if index_n == 0:
        return array[1]
    elif index_n == len(array) - 1:
        return array[-2]
    else:
        if n - array[index_n - 1] <= array[index_n + 1] - n:
            return array[index_n - 1]
        else:
            return array[index_n + 1]