def solution(my_string):
    nums = []
    i_sign = []
    current = 0
    new_my_string = my_string[::]
    
    for word in my_string:
        if new_my_string.find('+') == -1 and new_my_string.find('-') == -1:
            nums.append(int(new_my_string))
            break
        else:
            if word == '+':
                i_sign.append("+")
                nums.append(int(new_my_string[:current - 1]))
                new_my_string = new_my_string[current + 2:]
                current = -2
            if word == '-':
                i_sign.append("-")
                nums.append(int(new_my_string[:current - 1]))
                new_my_string = new_my_string[current + 2:]
                current = -2
            current += 1
    answer = nums[0]
    for i in range(len(i_sign)):
        if i_sign[i] == '+':
            answer += nums[i + 1]
        if i_sign[i] == '-':
            answer -= nums[i + 1]

    return answer

solution("10 - 8 + 2 - 2")
# "-", "+", "-"
# 10, 8, 2, 2