def solution(age):
    answer = ''
    trans_num={0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j'}
    answer=''.join(trans_num[int(x)] for x in str(age))
    return answer