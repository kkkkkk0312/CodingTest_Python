def solution(myString, pat):
    pat=pat.upper()
    myString=myString.upper()
    if pat in myString:
        return 1
    else:
        return 0
