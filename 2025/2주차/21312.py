# 칵테일은 주어진 3개의 숫자 중 최소 하나의 음료를 사용해야 함.
# 홀수 * 홀수 = 홀수, 짝수 * 짝수 = 짝수, 홀수 * 짝수 = 짝수
# 홀수 > 짝수
# 홀수, 짝수가 같으면 수가 더 큰 것
# AB, AC, BC
# 1. A, B, C, 중 홀수가 하나인 경우 -> 그 하나인 홀수
# 2. A, B, C, 중 홀수가 하나 이상인 경우 -> 홀수들 끼리 곱하기 
# 3. A, B, C, 중 홀수가 없는 경우 -> 모두 곱하기

A, B, C = map(int, input().split())
odd = []
even = []
for i in [A, B, C]:
    if i % 2 == 1:
        odd.append(i)
    else:
        even.append(i)
        
if len(odd) == 0:
    best_cocktail = A * B * C
elif len(odd) >= 1:
    best_cocktail = 1
    for i in odd:
        best_cocktail *= i

print(best_cocktail)

# if A % 2 == 1  and B % 2 == 1 and C % 2 == 1:
#     best_cocktail = A * B * C
# elif A % 2 == 1 and B % 2 == 1:
#     best_cocktail = A * B
# elif A % 2 == 1 and C % 2 == 1:
#     best_cocktail = A * C
# elif B % 2 == 1 and C % 2 == 1:
#     best_cocktail = B * C
# else:
#     best_cocktail = A * B * C
    
# print(best_cocktail)