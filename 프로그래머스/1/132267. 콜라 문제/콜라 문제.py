def solution(a, b, n):
    answer = 0
    cnt=0
    fn=0
    fcnt=0
    while (n+cnt)>=a:
        answer=answer+((n+cnt)//a)*b #받는 병의 수
        fn=n
        fcnt=cnt
        cnt=(fn+cnt)%a  # 자투리 병의 수
        n=((n+fcnt)//a)*b  #이번에 받은 병의 수
        print(n,cnt,answer)
    return answer