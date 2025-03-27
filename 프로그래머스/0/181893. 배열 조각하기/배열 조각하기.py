def solution(arr, query):

    for a,b in enumerate(query):
        if a%2==0:
            arr=arr[:b+1]
        else:
            arr=arr[b:]
    return arr