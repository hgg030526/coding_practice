def solution(my_string):
    
    return my_string[::-1] # 자체가 문자열임

x = list(reversed(my_string)) #reversed() 혼자 못쓰임
''.join(x) #문자열로 됨
