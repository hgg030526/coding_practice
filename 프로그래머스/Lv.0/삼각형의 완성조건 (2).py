def solution(sides):
    # max(sides)-min(sides) < x < max(sides)+min(sides)
    # max(sides)+min(sides) - (max(sides)-min(sides)) -1
    return 2*min(sides) - 1
