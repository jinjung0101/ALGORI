# 차이 (거리가 제일 짧은 수)가 가장 작을 것을 찾아 그 수를 반환해야함.
def solution(array, n):
    sor_array = sorted(array)
    before = abs(sor_array[-1] - n)
    answer = 0

    if n in sor_array:
        return n
    else:
        for i, number in enumerate(sor_array):
            if abs(sor_array[i] - n) < before:
                answer = number
                before = abs(sor_array[i] - n)
                print(1,before)
            else:
                before = abs(sor_array[i] - n)
                print(2, before)
    return answer


solution([3, 10, 28], 20)