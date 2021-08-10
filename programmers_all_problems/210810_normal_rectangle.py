from math import gcd
def solution(w,h):
    max_num = gcd(w,h)
    small_w, small_h = w/max_num, h/max_num
    print(max_num)
    delete_box =  (small_w+small_h - 1) * max_num
    return w*h - delete_box
print(solution(3,3))