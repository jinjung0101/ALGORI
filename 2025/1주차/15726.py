a, b, c = map(int, input().split())
A = a * b / c
B = a / b * c

if A > B:
    print(int(A))
else:
    print(int(B))