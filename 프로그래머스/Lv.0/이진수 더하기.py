def binary_to_decimal(binary):
    dec = 0
    for i,b in enumerate(reversed(binary)):
        dec += int(b)*(2**i)

    return dec

def decimal_to_binary(dec):
    binary = ''

    while dec > 1:
        binary = str(dec%2) + binary
        dec //= 2

    binary = str(dec) + binary

    return binary

def solution(bin1, bin2):
    dec_result = binary_to_decimal(bin1) + binary_to_decimal(bin2)
    return decimal_to_binary(dec_result)


# 다른 풀이 : bin() 함수 사용..
def solution(bin1, bin2):
    dec1 = int(bin1, 2)  # int(문자열, 진법)
    dec2 = int(bin2, 2)
    result = bin(dec1 + dec2) # '0b~~~'
    return result[2:]
