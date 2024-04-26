def solution(myString, pat):
    myString=myString.replace('A','@').replace('B','A').replace('@','B')
    print(myString)
    if pat in myString:
        return 1
    else:
        return 0
