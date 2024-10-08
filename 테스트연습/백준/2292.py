def find_layer(n):
    if n == 1:
        return 1  # 첫 번째 방은 바로 중앙에 있으므로 1층
    layer = 1  # 시작 층
    total_rooms = 1  # 현재까지의 방 수

    while total_rooms < n:
        # 각 층마다 방이 6의 배수로 증가
        total_rooms += 6 * layer
        layer += 1

    return layer

n = int(input())
print(find_layer(n))


# 수학적 풀이

def find_layer_math(n):
    if n == 1:
        return 1  # 첫 번째 방은 중앙에 있으므로 1층
    layer = 0
    count = 1  # 시작점
    while True:
        count += 6 * layer  # 각 레이어마다 6개씩 증가
        layer += 1
        if count >= n:
            return layer

n = int(input())
print(find_layer_math(n))
