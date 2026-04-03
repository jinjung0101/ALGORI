def total_seconds(hour, minute, second):
    return hour * 3600 + minute * 60 + second

start_time = list(map(str, input().split()))
end_time = list(map(str, input().split()))

datetime_start = total_seconds(int(start_time[0]), int(start_time[2]), int(start_time[4]))
datetime_end = total_seconds(int(end_time[0]), int(end_time[2]), int(end_time[4]))

if datetime_end < datetime_start:
    datetime_end += 24 * 3600  

print(datetime_end - datetime_start)  # 시간 차이를 초 단위로 출력