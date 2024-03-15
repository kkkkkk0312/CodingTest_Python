def solution(arr, queries):
    cnt=0
    for i in queries:
        a,b=i
        cnt=arr[a]
        arr[a]=arr[b]
        arr[b]=cnt
    return arr