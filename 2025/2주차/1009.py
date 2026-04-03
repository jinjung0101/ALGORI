num =  int(input())
def computer(a, b):
    if b > 20:
        b = b%21

    answer = list(str(a ** b))
    if answer[-1] == '0':
        print(10)
    else:
        print(int(answer[-1]))

for i in range(num):
    a, b = map(int, input().split())
    computer(a, b)