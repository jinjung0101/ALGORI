def show_multi(nums):
    for a, b, c in nums[0]:
        for x, y, z in nums[1]:
            answer_1 = 100*a*z
            answer_2 = 10*b*z
            answer_3 = c*z
    return 


nums = 472, 385
show_multi(nums)

# 항상 3자리수가 들어온다. 각 수를 다음 입력된 수의 1,10,100의 자리수와 각각 곱하고 합한수를 출력한다. 