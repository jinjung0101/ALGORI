def solution(l, r):
    answer = []

    # if l < 5:
    #     answer.append(-1)
    # else:
    #     for i in range(l, r + 1):
    #         if i % 5 == 0:
    #             num_list = list(map(int, str(i)))
    #             if num_list[0] == 5:
    #                 if 1 not in num_list and 2 not in num_list and 3 not in num_list and 4 not in num_list and 6 not in num_list and 7 not in num_list and 8 not in num_list and 9 not in num_list:
    #                     answer.append(i)
    #             else:
    #                 continue
    #         else:
    #             continue
    for i in range(l, r + 1):
        new_num = str(i)
        if set(new_num) <= { '0', '5'}:
            answer.append(i)

    if len(answer) == 0:
        answer.append(-1)
    return answer

print(solution(1,5055))









