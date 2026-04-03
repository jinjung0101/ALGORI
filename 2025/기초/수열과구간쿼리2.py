def solution(arr, queries):
    answer = []
    for i in queries:
        temp_answer = []
        for j in arr[i[0]:i[1] + 1]:
            if i[2] < j:
                temp_answer.append(j)  
        if len(temp_answer) == 0:
            answer.append(-1)
        else:
            temp_answer.sort()
            answer.append(temp_answer[0])
    return answer