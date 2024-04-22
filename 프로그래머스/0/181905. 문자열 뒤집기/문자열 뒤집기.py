def solution(my_string, s, e):
    answer = []
    a=my_string[::-1]
    return my_string[:s]+a[len(my_string)-e-1:len(my_string)-s]+my_string[e+1:]