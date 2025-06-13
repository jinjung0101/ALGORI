# 기차의 속도 S,  파리의 속도 T, 처음 두 기차 사이의 거리 D
S, T, D = map(int, input().split())
print( int(D / (S*2) * T))