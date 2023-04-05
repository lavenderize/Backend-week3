# 5.

def print_max():
    a, b, c, d, e = map(int, input("정수 5개 입력(띄어쓰기로 구분):").split())
    a_list = [a, b, c, d, e]
    print(max(a_list))

print_max()
