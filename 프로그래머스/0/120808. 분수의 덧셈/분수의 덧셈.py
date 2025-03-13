from fractions import Fraction
def solution(numer1, denom1, numer2, denom2):
    answer = []
    a=numer1/denom1
    b=numer2/denom2
    z=a+b
    x=Fraction(z).limit_denominator()
    return [x.numerator, x.denominator]