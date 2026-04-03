def solution(numbers):
    while True: 
        try:
            int(numbers)
            break
        except:
            if "zero" in numbers:
                numbers = numbers.replace('zero', '0')
            elif 'one' in numbers:
                numbers = numbers.replace("one", "1")
            elif 'two' in numbers:
                numbers = numbers.replace("two", "2")
            elif 'three' in numbers:
                numbers = numbers.replace("three", "3")    
            elif 'four' in numbers:
                numbers = numbers.replace("four", "4")
            elif 'five' in numbers:
                numbers = numbers.replace("five", "5")
            elif 'six' in numbers:
                numbers = numbers.replace("six", "6")
            elif 'seven' in numbers:
                numbers = numbers.replace("seven", "7")
            elif 'eight' in numbers:
                numbers = numbers.replace("eight", "8")
            elif 'nine' in numbers:
                numbers = numbers.replace("nine", "9")
        
    return numbers

solution("one")


def solution(numbers):
    num_dic = {
        'zero' : '0',
        'one' : '1', 
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }
    
    for key, value in num_dic.items():
        numbers = numbers.replace(key, value)
        
    return int(numbers)