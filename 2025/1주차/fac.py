import timeit

setup_code = '''
def factorial_no_memo(num):
    if num < 0:
        return 'Error'
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial_no_memo(num - 1)

def factorial_with_memo(num):
    if num < 0:
        return 'Error'
    if num in memo:
        return memo[num]
    memo[num] = num * factorial_with_memo(num - 1)
    return memo[num]

nums = [5, 3, 5, 3, 5]
'''

# 메모이제이션 미사용 시간 측정
no_memo_time = timeit.timeit('''
[factorial_no_memo(num) for num in nums]
''', setup=setup_code, number=10000)

# 메모이제이션 사용 시간 측정
with_memo_time = timeit.timeit('''
memo = {0: 1, 1: 1}
[factorial_with_memo(num) for num in nums]
''', setup=setup_code, number=10000)

print(f'메모이제이션 미사용 시간: {no_memo_time}')
print(f'메모이제이션 사용 시간: {with_memo_time}')
