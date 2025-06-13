while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
        # 평균 == 중앙값
    else:
        C = []
        # C [0] A == (A+B+C)/3
        C.append(2 * A - B)
        # C [1] C == (A+B+C)/3
        C.append((A + B) / 2)
        # C [2] B == (A+B+C)/3  
        C.append(2 * B - A)

        print(min(C))