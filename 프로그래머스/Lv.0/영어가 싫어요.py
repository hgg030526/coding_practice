def solution(numbers):
    number_lst = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i,n in enumerate(number_lst):
        if n in numbers:
            numbers = numbers.replace(n,str(i))    # replace만 사용하면 수정이 안됨 꼭 배열에 저장해야함
    return int(numbers)
