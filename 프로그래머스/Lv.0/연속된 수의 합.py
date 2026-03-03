def solution(num, total):
    #등차수열 : total = [num*{(초항)+(초항+num-1)}] / 2
    a = int((2*total - num**2 + num) / (2*num))
    return [a+i for i in range(num)]
