#분수의 덧셈

from math import gcd

def solution(numer1, denom1, numer2, denom2):
    numerator = (denom1*numer2) + (numer1*denom2) 
    denominator = (denom1*denom2)
    gcd_value = gcd(numerator, denominator)
    answer = [numerator/gcd_value, denominator/gcd_value]
    return answer